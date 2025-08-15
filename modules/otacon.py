from dotenv import load_dotenv
load_dotenv()

import os
import openai
from termcolor import colored  # déjà dans requirements

# Chemin d'accès adapté à ta structure
from utils.llm_basic_context.kg_context_code_structure import KG_CONTEXT_CODE_STRUCTURE
from utils.llm_basic_context.kg_context_example_code import KG_CONTEXT_EXAMPLE_CODE
from utils.llm_basic_context.kg_context_rules import KG_CONTEXT_RULES

# ====== ENV par défaut ======
LLM_PROVIDER      = os.getenv("LLM_PROVIDER", "openai").lower()

OPENAI_MODELS_AVAILABLE = ["gpt-4o", "gpt-4o-mini"]  
OPENAI_API_KEY    = os.getenv("OPENAI_API_KEY", "")
DEFAULT_OAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

ASI1_MODELS_AVAILABLE = ["asi1-mini"]
ASI1_API_KEY      = os.getenv("ASI1_API_KEY", "")
ASI1_BASE_URL     = os.getenv("ASI1_BASE_URL", "https://api.asi1.ai/v1")
# ⚠️ lit désormais ASI1_MODEL (conforme à ton .env)
DEFAULT_ASI1_MODEL = os.getenv("ASI1_MODEL", "asi1-mini")

# Modèle par défaut selon provider
DEFAULT_MODEL = DEFAULT_ASI1_MODEL if LLM_PROVIDER == "asi1" else DEFAULT_OAI_MODEL
# =======================================================

class OTACON:
    """
    Agent central DECIMA pour :
      - Génération de réponses LLM (explication + code Python)
      - Injection du contexte EMMA (filtré) + contexte large structuré (code structure MCNPTools)
      - Dialogue expert MCNP PTRAC (pas de hors sujet)
    """

    def __init__(self, model: str = DEFAULT_MODEL):
        # --- inchangé : état courant ---
        self.model = model
        self.provider = LLM_PROVIDER
        self.api_key = None
        self.client = None

        # Construction du client selon provider par défaut (.env)
        self._configure_client(self.provider)

    def _configure_client(self, provider: str) -> None:
        """
        (interne) Configure le client HTTP selon le provider (openai | asi1)
        sans toucher au reste de ta logique.
        """
        provider = (provider or "openai").lower()
        self.provider = provider
        if provider == "asi1":
            # Client OpenAI-compatible mais avec base_url ASI1
            self.api_key = ASI1_API_KEY
            self.client = openai.OpenAI(api_key=self.api_key, base_url=ASI1_BASE_URL)
        else:
            self.api_key = OPENAI_API_KEY
            self.client = openai.OpenAI(api_key=self.api_key)

    def set_model_and_provider(self, model_name: str) -> None:
        m = (model_name or "").lower()
        provider = "asi1" if m.startswith("asi") else "openai"

        # Validation si provider == asi1
        if provider == "asi1" and m not in ASI1_MODELS_AVAILABLE:
            print(colored(f"[WARN] Modèle ASI1 inconnu : {model_name}. "
                        f"Modèles valides : {', '.join(ASI1_MODELS_AVAILABLE)}", "red"))
            # Option : forcer sur le modèle par défaut
            model_name = DEFAULT_ASI1_MODEL

        if provider == "openai" and m not in OPENAI_MODELS_AVAILABLE:  # 🆕
            print(colored(f"[WARN] Modèle OpenAI inconnu : {model_name}. "
                        f"Modèles valides : {', '.join(OPENAI_MODELS_AVAILABLE)}", "red"))
            model_name = DEFAULT_OAI_MODEL

        self.model = model_name
        self._configure_client(provider)
        print(colored(f"[INFO] Reconfig LLM: provider={self.provider} | model={self.model}",
                    "green" if self.provider == "asi1" else "cyan"))

        # 🔹 Vérification immédiate auprès de l’API du modèle réellement utilisé
        if self.provider == "asi1":
            try:
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": "ping"}],
                    max_tokens=1
                )
                real_model = getattr(resp, "model", None)
                if real_model and real_model != self.model:
                    print(colored(f"[WARN] L'API a fallback sur un autre modèle : {real_model}", "red"))
                else:
                    print(colored(f"[DEBUG] Modèle confirmé par l'API : {real_model}", "green"))
            except Exception as e:
                print(colored(f"[ERROR] Impossible de vérifier le modèle : {e}", "red"))

        
    def build_prompt(self, user_query: str, emma_context: dict, use_context: bool = True) -> str:
        prompt = []

        if use_context:
            prompt.extend([
                "Tu es OTACON, un agent MCNP PTRAC expert.",
                "Tu ne réponds qu’aux requêtes d’analyse ou parsing de fichiers PTRAC issus de MCNP, en utilisant exclusivement la librairie mcnptools.",
                "",
                "---",
                "CONTEXTE :",
                "Tu disposes de deux sources de contexte :",
                "1. Contexte EMMA : une liste d'entités candidates extraites automatiquement du graphe de connaissances (KG).",
                "   Cette liste constitue un bon point de départ : les entités les plus pertinentes y sont souvent présentes.",
                "   Toutefois, elle peut contenir des erreurs (faux positifs, faux négatifs). Tu dois donc l'utiliser comme une aide à la décision, pas comme une vérité absolue.",
                "2. Contexte large structuré : description exhaustive des classes, méthodes, enums et structures de mcnptools (fiable).",
                "   Si EMMA est incomplet ou erroné, tu peux t’appuyer uniquement sur ce contexte structuré.",
                "",
            ])

            # Ajout des règles
            prompt.append(KG_CONTEXT_RULES.strip())
            prompt.append("")

            # Contexte EMMA
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
                prompt.append("(Pas d'entités EMMA détectées pour cette requête.)")

            prompt.append("")
            prompt.append("# Contexte large structuré (API et enums MCNPTools, à utiliser si besoin ou pour validation croisée)")
            prompt.append(KG_CONTEXT_CODE_STRUCTURE.strip())
            prompt.append("")

            prompt.append("# Exemple typique d'analyse simple d'un fichier PTRAC MCNP avec mcnptools")
            prompt.append(KG_CONTEXT_EXAMPLE_CODE.strip())
            prompt.append("")

        else:
            prompt.append("Answer my query in relation to the attached PTRAC file, using Python and the mcnptools library.")
            prompt.append("")

        prompt.append("# Requête utilisateur :")
        prompt.append(user_query)
        prompt.append("")

        return "\n".join(prompt)

    def ask_llm(self, prompt: str, temperature: float = 0.2, max_tokens: int = 2000) -> str:
    # Log de l'endpoint actif pour debug
        try:
            base_url = getattr(self.client, "_base_url", None) or getattr(self.client, "base_url", None)
            color = "green" if self.provider == "asi1" else "yellow"
            print(colored(f"[DEBUG] Endpoint API : {base_url}", color))
        except Exception:
            pass
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": (
                    "Tu es un agent expert MCNP PTRAC. Réponds uniquement à des questions de parsing/analyse de fichiers PTRAC MCNP. "
                    "Le contexte EMMA est un guidage, pas une vérité absolue. Utilise le contexte large structuré si besoin. "
                    "Fournis toujours d’abord une explication, puis un code Python dans un bloc ```python."
                )},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    def parse_llm_output(self, llm_output: str) -> dict:
        import re
        code = ""
        explanation = llm_output
        m = re.search(r"```python(.*?)```", llm_output, re.DOTALL)
        if m:
            code = m.group(1).strip()
            explanation = (
                llm_output[: m.start()].strip() + llm_output[m.end() :].strip()
            )
        return {
            "explanation": explanation.strip(),
            "code": code,
            "raw_output": llm_output,
        }

    def run(self, user_query: str, emma_context: dict) -> dict:
        # Print en temps réel le modèle qui va être utilisé
        provider_msg = f"[INFO] LLM utilisé pour cette requête : {self.provider} (modèle: {self.model})"
        print(colored(provider_msg, "cyan" if self.provider == "openai" else "green"))

        use_context = emma_context.get("use_context", True)
        prompt = self.build_prompt(user_query, emma_context, use_context=use_context)
        print("======= PROMPT LLM =======\n", prompt)
        llm_output = self.ask_llm(prompt)
        result = self.parse_llm_output(llm_output)
        return result

if __name__ == "__main__":
    user_query = (
        "Nombre total de neutrons, photons et photons de réactions photo-nucléaires traversant la cellule 200 représentant le fût"
    )
    emma_context = {
        "entities": [
            # … liste structurée d’entités (voir sortie EMMAAgent) …
        ]
    }
    agent = OTACON()
    output = agent.run(user_query, emma_context)
    print("[EXPLICATION]")
    print(output["explanation"])
    print("[CODE PYTHON]")
    print(output["code"])
