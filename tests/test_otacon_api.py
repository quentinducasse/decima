# tests/test_otacon_agent_api.py

from dotenv import load_dotenv
load_dotenv()  # Automatically load variables from .env into environment

import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
        error_msg = str(e)
        print(f"\n[FAIL] Error during OpenAI call: {error_msg}")

        # Provide helpful guidance based on error type
        if "api_key" in error_msg.lower() or "authentication" in error_msg.lower():
            print("\nTIP: Check that your OPENAI_API_KEY is valid and has credits.")
            print("     You can check your API key at: https://platform.openai.com/api-keys")
        elif "rate_limit" in error_msg.lower():
            print("\nTIP: You've hit the OpenAI rate limit. Wait a moment and try again.")
        elif "connection" in error_msg.lower() or "timeout" in error_msg.lower():
            print("\nTIP: Check your internet connection.")

        return False


if __name__ == "__main__":
    test_otacon_api_key()
