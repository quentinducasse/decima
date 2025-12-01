"""
DECIMA - Data Extraction & Contextual Inference for MCNP Analysis

A framework combining LLMs and Knowledge Graphs for analyzing MCNP PTRAC files
through natural language queries.

Basic usage:
    >>> from decima import DECIMA
    >>>
    >>> # Initialize analyzer
    >>> analyzer = DECIMA(openai_api_key='your-key')
    >>>
    >>> # Analyze a PTRAC file
    >>> result = analyzer.analyze(
    ...     ptrac_path='data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac',
    ...     query='Plot the energy distribution of neutrons'
    ... )
    >>>
    >>> # Access results
    >>> print(result['explanation'])  # Natural language explanation
    >>> print(result['code'])         # Generated Python code
    >>> print(result['stdout'])       # Execution output

For more examples, see the examples/ directory.
"""

__version__ = "1.2.0"
__author__ = "Quentin Ducasse, Feda Almuhisen"
__license__ = "Apache-2.0"

import os
import sys
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

# Add parent directory to path to allow imports
_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

# Import core modules
from modules.campbell import CampbellOrchestrator
from modules.quiet import QUIET
from modules.emma import EMMA
from modules.otacon import OTACON
from modules.eva import EVA
from kg.loader.neo4j_loader import Neo4jTripletMigrator, get_neo4j_driver


def _check_kg_loaded(uri: str, user: str, password: str) -> bool:
    """Check if Knowledge Graph is already loaded in Neo4j."""
    try:
        driver = get_neo4j_driver(uri, user, password)
        with driver.session() as session:
            result = session.run("MATCH (n) RETURN count(n) as count")
            count = result.single()["count"]
            driver.close()
            return count > 0
    except Exception as e:
        logger.warning(f"Could not check KG status: {e}")
        return False


def _load_kg(uri: str, user: str, password: str, triplets_dir: str) -> bool:
    """Load Knowledge Graph triplets into Neo4j."""
    try:
        migrator = Neo4jTripletMigrator(uri, user, password)
        if migrator.connect():
            logger.info("Loading Knowledge Graph into Neo4j...")
            migrator.migrate_all_triplets(triplets_dir)
            migrator.close()
            logger.info("Knowledge Graph loaded successfully.")
            return True
        return False
    except Exception as e:
        logger.error(f"Failed to load Knowledge Graph: {e}")
        return False


def setup_knowledge_graph(
    uri: str = None,
    user: str = None,
    password: str = None,
    triplets_dir: str = None,
    force_reload: bool = False
) -> bool:
    """
    Setup the Knowledge Graph in Neo4j.

    This function checks if the KG is already loaded and loads it if necessary.
    Can be called manually or is called automatically by DECIMA.__init__.

    Args:
        uri: Neo4j URI (default: bolt://localhost:7687)
        user: Neo4j user (default: neo4j)
        password: Neo4j password (default: decima123)
        triplets_dir: Path to triplets directory (default: kg/triplets)
        force_reload: Force reload even if KG is already loaded

    Returns:
        True if KG is ready, False otherwise
    """
    uri = uri or os.getenv("NEO4J_URI", "bolt://neo4j:7687")
    user = user or os.getenv("NEO4J_USER", "neo4j")
    password = password or os.getenv("NEO4J_PASSWORD", "decima123")
    triplets_dir = triplets_dir or os.path.join(_parent_dir, "kg", "triplets")

    if not force_reload and _check_kg_loaded(uri, user, password):
        logger.info("Knowledge Graph already loaded.")
        return True

    return _load_kg(uri, user, password, triplets_dir)


class DECIMA:
    """
    Main DECIMA interface for programmatic analysis of MCNP PTRAC files.

    This class provides a simple Python API for analyzing PTRAC files using
    natural language queries. It orchestrates the QUIET, EMMA, OTACON, and EVA
    modules through the CAMPBELL orchestrator.

    Attributes:
        campbell: The CAMPBELL orchestrator managing the workflow

    Example:
        >>> # Basic usage
        >>> analyzer = DECIMA(openai_api_key='sk-...')
        >>> result = analyzer.analyze(
        ...     ptrac_path='file.ptrac',
        ...     query='Show collision energies for first 20 histories'
        ... )
        >>> print(result['explanation'])
        >>> print(result['code'])

        >>> # Use demo mode (no API key required)
        >>> analyzer = DECIMA()  # Will use demo mode
        >>> result = analyzer.analyze('file.ptrac', 'your query')
    """

    def __init__(
        self,
        openai_api_key: Optional[str] = None,
        neo4j_uri: Optional[str] = None,
        neo4j_user: Optional[str] = None,
        neo4j_password: Optional[str] = None,
        demo_mode: bool = False,
        auto_load_kg: bool = True
    ):
        """
        Initialize DECIMA analyzer.

        Args:
            openai_api_key: OpenAI API key (optional, uses OPENAI_API_KEY env var if not provided)
            neo4j_uri: Neo4j database URI (optional, uses NEO4J_URI env var or default)
            neo4j_user: Neo4j username (optional, uses NEO4J_USER env var or default)
            neo4j_password: Neo4j password (optional, uses NEO4J_PASSWORD env var or default)
            demo_mode: Enable demo mode (returns fixed example without LLM)
            auto_load_kg: Automatically load Knowledge Graph if not already loaded (default: True)

        Note:
            If no API key is provided and demo_mode is False, DECIMA will automatically
            run in demo mode.
        """
        # Set API key in environment if provided
        if openai_api_key:
            os.environ['OPENAI_API_KEY'] = openai_api_key

        # Set demo mode - only if explicitly requested OR no API key available
        if demo_mode:
            os.environ['DEMO_MODE'] = 'true'
        elif not openai_api_key and not os.getenv('OPENAI_API_KEY'):
            os.environ['DEMO_MODE'] = 'true'
        else:
            # Make sure demo mode is disabled when we have an API key
            os.environ.pop('DEMO_MODE', None)

        # Auto-load Knowledge Graph if enabled
        if auto_load_kg:
            setup_knowledge_graph(
                uri=neo4j_uri,
                user=neo4j_user,
                password=neo4j_password
            )

        # Initialize the CAMPBELL orchestrator
        self.campbell = CampbellOrchestrator(otacon_api_key=openai_api_key)

    def analyze(
        self,
        ptrac_path: str,
        query: str,
        use_context: bool = True,
        model: str = 'gpt-4o-mini'
    ) -> Dict[str, Any]:
        """
        Analyze a PTRAC file using a natural language query.

        This method:
        1. Interprets the query using QUIET (language detection, keyword extraction)
        2. Enriches context using EMMA (Knowledge Graph lookup)
        3. Generates explanation and code using OTACON (LLM reasoning)
        4. Executes code safely using EVA (sandboxed execution)

        Args:
            ptrac_path: Path to the PTRAC file (ASCII or binary format)
            query: Natural language question in English or French
                   Examples:
                   - "Plot energy distribution of neutrons"
                   - "Show collision positions for first 20 histories"
                   - "What is the average energy of secondary photons?"
            use_context: Enable Knowledge Graph context injection (default: True)
            model: LLM model to use ('gpt-4o-mini' or 'gpt-4o', default: 'gpt-4o-mini')

        Returns:
            Dictionary containing:
            - 'explanation': Natural language explanation of the analysis
            - 'code': Generated Python code using mcnptools
            - 'stdout': Standard output from code execution
            - 'stderr': Standard error from code execution (if any)
            - 'plots': List of generated plot file paths
            - 'error': Error message (if execution failed)
            - 'logs': List of workflow log messages

        Raises:
            FileNotFoundError: If ptrac_path does not exist
            ValueError: If query is empty or invalid

        Example:
            >>> result = analyzer.analyze(
            ...     ptrac_path='data/file.ptrac',
            ...     query='Plot the W distribution of source particles'
            ... )
            >>> print(result['explanation'])
            >>> print(result['code'])
            >>> if result['plots']:
            ...     print(f"Generated plots: {result['plots']}")
        """
        # Validate inputs
        if not os.path.exists(ptrac_path):
            raise FileNotFoundError(f"PTRAC file not found: {ptrac_path}")

        if not query or not query.strip():
            raise ValueError("Query cannot be empty")

        # Set model if needed
        if hasattr(self.campbell.otacon_agent, 'model'):
            self.campbell.otacon_agent.model = model

        # Process the query through CAMPBELL orchestrator
        result = self.campbell.process_query(
            query=query,
            ptrac_path=ptrac_path,
            use_context=use_context
        )

        return result

    def get_version(self) -> str:
        """Return DECIMA version string."""
        return __version__


# Expose main classes for advanced usage
__all__ = [
    'DECIMA',
    'setup_knowledge_graph',
    'CampbellOrchestrator',
    'QUIET',
    'EMMA',
    'OTACON',
    'EVA',
]
