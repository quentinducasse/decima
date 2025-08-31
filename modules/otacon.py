"""
DECIMA Agent - OTACON - Operator for Assisted Communication & Output Navigation
Central LLM engine for PTRAC parsing, code generation, and expert reasoning with structured + KG context
"""

from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

# Load environment variables depending on local/docker deployment
if os.path.exists(".env.local"):
    load_dotenv(".env.local")
elif os.path.exists(".env.docker"):
    load_dotenv(".env.docker")
else:
    load_dotenv()

import openai

from utils.llm_basic_context.kg_context_code_structure import KG_CONTEXT_CODE_STRUCTURE
from utils.llm_basic_context.kg_context_example_code import KG_CONTEXT_EXAMPLE_CODE
from utils.llm_basic_context.kg_context_rules import KG_CONTEXT_RULES

# ====== ENV defaults ======
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()

OPENAI_MODELS_AVAILABLE = ["gpt-4o", "gpt-4o-mini"]
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEFAULT_OAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

ASI1_MODELS_AVAILABLE = ["asi1-mini"]
ASI1_API_KEY = os.getenv("ASI1_API_KEY", "")
ASI1_BASE_URL = os.getenv("ASI1_BASE_URL", "https://api.asi1.ai/v1")
DEFAULT_ASI1_MODEL = os.getenv("ASI1_MODEL", "asi1-mini")

# Default model depending on provider
DEFAULT_MODEL = DEFAULT_ASI1_MODEL if LLM_PROVIDER == "asi1" else DEFAULT_OAI_MODEL
# =======================================================


class OTACON:
    """
    Central DECIMA agent for:
      - Generating LLM responses (explanations + Python code)
      - Injecting EMMA context (filtered KG) + large structured context (MCNPTools code structure)
      - Acting as an expert dialogue engine for PTRAC parsing/analysis
    """

    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model
        self.provider = LLM_PROVIDER
        self.api_key = None
        self.client = None

        # Configure client according to default provider
        self._configure_client(self.provider)

    def _configure_client(self, provider: str) -> None:
        """
        Internal: configure the HTTP client according to provider (openai | asi1).
        """
        provider = (provider or "openai").lower()
        self.provider = provider
        if provider == "asi1":
            self.api_key = ASI1_API_KEY
            self.client = openai.OpenAI(api_key=self.api_key, base_url=ASI1_BASE_URL)
        else:
            self.api_key = OPENAI_API_KEY
            self.client = openai.OpenAI(api_key=self.api_key)

    def set_model_and_provider(self, model_name: str) -> None:
        """
        Switch provider/model dynamically based on model name provided by frontend or config.
        """
        m = (model_name or "").lower()
        provider = "asi1" if m.startswith("asi") else "openai"

        # Validation for ASI1
        if provider == "asi1" and m not in ASI1_MODELS_AVAILABLE:
            logger.warning(f"[WARN] Unknown ASI1 model: {model_name}. Valid models: {', '.join(ASI1_MODELS_AVAILABLE)}")
            model_name = DEFAULT_ASI1_MODEL

        # Validation for OpenAI
        if provider == "openai" and m not in OPENAI_MODELS_AVAILABLE:
            logger.warning(f"[WARN] Unknown OpenAI model: {model_name}. Valid models: {', '.join(OPENAI_MODELS_AVAILABLE)}")
            model_name = DEFAULT_OAI_MODEL

        self.model = model_name
        self._configure_client(provider)

        logger.info(f"[INFO] Reconfig LLM: provider={self.provider} | model={self.model}")

        # Optional: check with API if model is actually available (only for ASI1)
        if self.provider == "asi1":
            try:
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": "ping"}],
                    max_tokens=1
                )
                real_model = getattr(resp, "model", None)
                if real_model and real_model != self.model:
                    logger.warning(f"[WARN] API fallback to another model: {real_model}")
                else:
                    logger.debug(f"[DEBUG] Model confirmed by API: {real_model}")
            except Exception as e:
                logger.error(f"[ERROR] Could not verify model: {e}")

    def build_prompt(self, user_query: str, emma_context: dict, use_context: bool = True) -> str:
        """
        Build the system prompt sent to the LLM. Combines EMMA KG context with structured code context.
        """
        prompt = []

        if use_context:
            prompt.extend([
                "You are OTACON, an expert MCNP PTRAC agent.",
                "You only answer requests related to analysis or parsing of MCNP PTRAC files, exclusively using the mcnptools library.",
                "",
                "---",
                "CONTEXT:",
                "You have two sources of context:",
                "1. EMMA context: a list of candidate entities extracted automatically from the knowledge graph (KG).",
                "   This list is a good starting point but may contain errors (false positives/negatives). Use it as guidance, not absolute truth.",
                "2. Large structured context: exhaustive description of classes, methods, enums, and structures of mcnptools (reliable).",
                "   If EMMA is incomplete or wrong, you may rely solely on this structured context.",
                "",
            ])

            # Add KG rules
            prompt.append(KG_CONTEXT_RULES.strip())
            prompt.append("")

            # EMMA KG context
            if emma_context and "entities" in emma_context and emma_context["entities"]:
                prompt.append("[KG CONTEXT EMMA]")
                for ent in emma_context["entities"]:
                    s = f"- id: {ent['id']}, type: {ent.get('type', '')}"
                    if ent.get("parent_dict"):
                        s += f", parent_dict: {ent['parent_dict']}"
                    if ent.get("parent_enum"):
                        s += f", parent_enum: {ent['parent_enum']}"
                    if ent.get("parent_class"):
                        s += f", parent_class: {ent['parent_class']}"
                    if ent.get("value") is not None:
                        s += f", value: {ent['value']}"
                    if ent.get("score") is not None:
                        s += f", score: {ent['score']}"
                    if ent.get("description"):
                        s += f", description: {ent['description'][:150].replace(chr(10),' ')}"
                    prompt.append(s)
            else:
                prompt.append("(No EMMA entities detected for this query.)")

            prompt.append("")
            prompt.append("# Large structured context (MCNPTools API + enums, use if needed or for cross-validation)")
            prompt.append(KG_CONTEXT_CODE_STRUCTURE.strip())
            prompt.append("")

            prompt.append("# Example of typical analysis of a PTRAC file using mcnptools")
            prompt.append(KG_CONTEXT_EXAMPLE_CODE.strip())
            prompt.append("")

        else:
            prompt.append("Answer the query in relation to the attached PTRAC file, using Python and the mcnptools library.")
            prompt.append("")

        prompt.append("# User query:")
        prompt.append(user_query)
        prompt.append("")

        return "\n".join(prompt)

    def ask_llm(self, prompt: str, temperature: float = 0.2, max_tokens: int = 3000) -> str:
        """
        Send the prompt to the LLM and return the generated response.
        """
        try:
            base_url = getattr(self.client, "_base_url", None) or getattr(self.client, "base_url", None)
            logger.debug(f"[DEBUG] Endpoint API : {base_url}")
        except Exception:
            pass
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system",
                     "content": (
                         "You are an expert MCNP PTRAC agent. Only answer questions about parsing/analysis of MCNP PTRAC files. "
                         "EMMA context is guidance, not absolute truth. Use structured context if needed. "
                         "Always provide first an explanation, then Python code inside a ```python block."
                     )},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content

        except Exception as e:
            err_msg = str(e)
            if "401" in err_msg or "Unauthorized" in err_msg:
                return "[ERROR:INVALID_API_KEY] Your API key is invalid or unauthorized. Please check your `.env` file and update `OPENAI_API_KEY`."
            return f"[ERROR] LLM request failed: {err_msg}"

    def parse_llm_output(self, llm_output: str) -> dict:
        """
        Parse the LLM output into explanation + code block.
        """
        import re
        code = ""
        explanation = llm_output
        m = re.search(r"```python(.*?)```", llm_output, re.DOTALL)
        if m:
            code = m.group(1).strip()
            explanation = (
                llm_output[: m.start()].strip() + llm_output[m.end():].strip()
            )
        return {
            "explanation": explanation.strip(),
            "code": code,
            "raw_output": llm_output,
        }

    def run(self, user_query: str, emma_context: dict) -> dict:
        """
        Run the complete OTACON pipeline: build prompt, send to LLM, parse output.
        """
        logger.info(f"[INFO] LLM used for this request: {self.provider} (model: {self.model})")

        use_context = emma_context.get("use_context", True)
        prompt = self.build_prompt(user_query, emma_context, use_context=use_context)

        # Verbose logging of context parts
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("[OTACON] EMMA context:\n%s", emma_context)
            logger.debug("======= FULL PROMPT SENT TO LLM =======\n%s", prompt)

        llm_output = self.ask_llm(prompt)
        result = self.parse_llm_output(llm_output)
        return result


if __name__ == "__main__":
    user_query = (
        "What are the x, y, z positions, energy, and time of collision events?"
    )
    emma_context = {"entities": []}
    agent = OTACON()
    output = agent.run(user_query, emma_context)

    logger.info("[EXPLANATION]\n%s", output["explanation"])
    logger.info("[PYTHON CODE]\n%s", output["code"])
