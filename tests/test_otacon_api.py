# tests/test_otacon_agent_api.py

from dotenv import load_dotenv
load_dotenv()  # Automatically load variables from .env into environment

import os
from modules.otacon import OTACON

# --- Early check before running anything ---
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or not api_key.startswith("sk-"):
    print(
        "\n[ERROR] OPENAI_API_KEY is not set correctly!\n"
        "Please edit your .env.docker (or .env.local) and set a valid OpenAI API key.\n"
        "Example:\n"
        "    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
        f"Current OPENAI_API_KEY = {api_key}\n"
    )
    exit(1)


def test_otacon_api_key():
    """Basic integration test: checks that OTACON can call the LLM with the provided API key."""
    agent = OTACON()
    user_query = "Give me an example of using mcnptools to parse a PTRAC file."
    emma_context = {"entities": []}  # No filtered context

    try:
        print("[INFO] Testing LLM call via OTACON...")
        result = agent.run(user_query, emma_context)
        print("\n[OPENAI/OTACON OK] LLM explanation:")
        print(result["explanation"][:400] + " [...]")
        print("\nCode block extracted by parsing:")
        print(result["code"][:400] + " [...]")
        print("\n[SUCCESS] API key and LLM access confirmed.\n")
        return True
    except Exception as e:
        print(f"[FAIL] Error during OpenAI call: {e}")
        return False


if __name__ == "__main__":
    test_otacon_api_key()
