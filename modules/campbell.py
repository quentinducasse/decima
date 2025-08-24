"""
DECIMA Orchestrator - CAMPBELL - Coordination & Assignment Manager for Process Balancing & Execution Logistics Layer
Robust orchestration of EVA, OTACON, EMMA, QUIET modules via LangGraph
"""
from dotenv import load_dotenv
import os

if os.path.exists(".env.local"):
    load_dotenv(".env.local")
elif os.path.exists(".env.docker"):
    load_dotenv(".env.docker")
else:
    load_dotenv()

import json
import logging
from typing import Dict, List, Any, Optional, TypedDict
from enum import Enum
from langgraph.graph import StateGraph, END

# Import DECIMA modules
from modules.quiet import QUIET
from modules.emma import EMMA
from modules.otacon import OTACON
from modules.eva import EVA

logger = logging.getLogger(__name__)

class AgentState(TypedDict):
    query: str
    language: str
    query_type: str
    focus_events: List[str]
    focus_data: List[str]
    focus_dictionaries: List[str]
    focus_classes: List[str]
    focus_methods: List[str]
    focus_attributes: List[str]
    entities: List[Dict[str, Any]]
    context: Dict[str, Any]
    response: str
    code: Optional[str]
    ptrac_path: Optional[str]
    execution_result: Optional[dict]
    error: Optional[str]
    logs: List[str]
    status: str
    use_context: bool

class CampbellOrchestrator:
    """
    Main DECIMA orchestrator (CAMPBELL).
    Handles workflow execution between QUIET, EMMA, OTACON, EVA agents.
    """
    def __init__(self, otacon_api_key: Optional[str] = None):
        self.quiet_agent = QUIET()
        self.emma_agent = EMMA()
        self.otacon_agent = OTACON()
        self.eva_agent = EVA()
        self.workflow = self._create_workflow()
        self.app = self.workflow.compile()

    def _create_workflow(self) -> StateGraph:
        workflow = StateGraph(AgentState)
        workflow.add_node("quiet", self._run_quiet_agent)
        workflow.add_node("emma", self._run_emma_agent)
        workflow.add_node("otacon", self._run_otacon_agent)
        workflow.add_node("eva", self._run_eva_agent)

        # Workflow transitions
        workflow.add_edge("quiet", "emma")
        workflow.add_edge("emma", "otacon")
        workflow.add_conditional_edges("otacon", self._route_after_otacon, {
            "eva": "eva",
            "end": END
        })
        workflow.add_edge("eva", END)

        workflow.set_entry_point("quiet")
        return workflow

    # === QUIET NODE ===
    def _run_quiet_agent(self, state: AgentState) -> AgentState:
        logger.info("Running QUIET")
        try:
            q_out = self.quiet_agent.analyze(state["query"])
            state["language"] = q_out.get("language", "")
            state["query_type"] = q_out.get("query_type", "")
            state["focus_events"] = q_out.get("focus_events", [])
            state["focus_data"] = q_out.get("focus_data", [])
            state["focus_dictionaries"] = q_out.get("focus_dictionaries", [])
            state["focus_classes"] = q_out.get("focus_classes", [])
            state["focus_methods"] = q_out.get("focus_methods", [])
            state["focus_attributes"] = q_out.get("focus_attributes", [])
            state["logs"].append("[QUIET] OK")
            state["status"] = "quiet_done"
        except Exception as e:
            state["error"] = f"[QUIET ERROR] {str(e)}"
            state["status"] = "error"
            state["logs"].append(state["error"])
        return state

    # === EMMA NODE ===
    def _run_emma_agent(self, state: AgentState) -> AgentState:
        if not state.get("use_context", True):
            logger.info("Add context disabled — skipping EMMA.")
            prefix = (
                "Answer my query in relation to the attached PTRAC file, "
                "using Python and the mcnptools library."
            )
            state["query"] = f"{prefix}\n\nUser query: {state['query']}"
            state["context"] = {}
            state["entities"] = []
            state["logs"].append("[EMMA] Skipped (Add context off)")
            state["status"] = "emma_skipped"
            return state

        logger.info("Running EMMA")
        try:
            quiet_context = {
                "query": state["query"],
                "language": state["language"],
                "focus_events": state["focus_events"],
                "focus_data": state.get("focus_data", []),
                "focus_dictionaries": state.get("focus_dictionaries", []),
                "focus_classes": state.get("focus_classes", []),
                "focus_methods": state.get("focus_methods", []),
                "focus_attributes": state.get("focus_attributes", []),
            }
            emma_context = self.emma_agent.extract_kg_context(quiet_context)
            state["context"] = emma_context
            state["entities"] = emma_context.get("entities", [])
            if not state["entities"]:
                state["error"] = "[EMMA WARNING] No entities detected. Check if Neo4j Desktop is running and the DECIMA graph is started."
                state["logs"].append(state["error"])
            else:
                state["logs"].append("[EMMA] OK")
            state["status"] = "emma_done"
        except Exception as e:
            state["error"] = f"[EMMA ERROR] {str(e)}"
            state["status"] = "error"
            state["logs"].append(state["error"])
        return state

    # === OTACON NODE ===
    def _run_otacon_agent(self, state: AgentState) -> AgentState:
        logger.info("Running OTACON")
        try:
            result = self.otacon_agent.run(
                user_query=state["query"],
                emma_context={**state["context"], "use_context": state.get("use_context", True)}
            )
            state["response"] = result.get("explanation", "")
            state["code"] = result.get("code", "")
            state["logs"].append("[OTACON] OK")
            state["status"] = "otacon_done"

            if state.get("error") and "No entities detected" in state["error"]:
                state["response"] = ""
                state["code"] = ""
        except Exception as e:
            state["error"] = f"[OTACON ERROR] {str(e)}"
            state["status"] = "error"
            state["logs"].append(state["error"])
        return state

    # === EVA NODE ===
    def _run_eva_agent(self, state: AgentState) -> AgentState:
        logger.info("Running EVA")
        try:
            if not state.get("ptrac_path"):
                state["error"] = "[EVA] No PTRAC path provided in state."
                state["logs"].append(state["error"])
                state["status"] = "eva_missing_ptrac"
                return state
            if not state.get("code"):
                state["error"] = "[EVA] No code to execute (OTACON generated nothing)."
                state["logs"].append(state["error"])
                state["status"] = "eva_missing_code"
                return state

            loaded = self.eva_agent.load_file(state["ptrac_path"])
            if not loaded:
                state["error"] = f"[EVA] PTRAC file not found: {state['ptrac_path']}"
                state["logs"].append(state["error"])
                state["status"] = "eva_file_not_found"
                return state

            exec_result = self.eva_agent.execute_code(state["code"], language="python")
            state["execution_result"] = exec_result
            state["logs"].append("[EVA] OK")
            state["status"] = "eva_done"
        except Exception as e:
            state["error"] = f"[EVA ERROR] {str(e)}"
            state["status"] = "error"
            state["logs"].append(state["error"])
        return state

    # === TRANSITIONS ===
    def _route_after_otacon(self, state: AgentState) -> str:
        """
        If OTACON generated code and a PTRAC path is provided, run EVA, otherwise end workflow.
        """
        if state.get("code") and state.get("ptrac_path"):
            return "eva"
        return "end"

    # === MAIN API ===
    def process_query(self, query: str, ptrac_path: Optional[str] = None, use_context: bool = True) -> Dict[str, Any]:
        """
        Launch the entire workflow with the user query and an optional PTRAC path.
        """
        initial_state: AgentState = {
            "query": query,
            "language": "",
            "query_type": "",
            "focus_events": [],
            "focus_data": [],
            "focus_dictionaries": [],
            "focus_classes": [],
            "focus_methods": [],
            "focus_attributes": [],
            "entities": [],
            "context": {},
            "response": "",
            "code": None,
            "ptrac_path": ptrac_path,
            "execution_result": None,
            "error": None,
            "logs": [],
            "status": "initialized",
            "use_context": use_context
        }

        logger.info(f"Starting workflow for query: {query} (PTRAC={ptrac_path})")
        result = self.app.invoke(initial_state)
        return result

if __name__ == "__main__":
    orchestrator = CampbellOrchestrator()
    test_ptrac = r"path/to/your/ptracFile"
    test_query = "What are the x, y, z positions, energy, and time of collision events?"
    result = orchestrator.process_query(test_query, ptrac_path=test_ptrac)
    print(json.dumps(result, indent=2, ensure_ascii=False))
