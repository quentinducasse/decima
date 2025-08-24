# tests/test_eva.py

from dotenv import load_dotenv
load_dotenv()
import os
import unittest
from modules.eva import EVA

# === Path to the PTRAC file used for testing ===
# ⚠️ IMPORTANT: Replace this path with the location of your own PTRAC file
PTRAC_FILE = r"C:\Users\username\path\to\your\ptrac_file.ptrac"

# --- Early check before running any tests ---
if "username" in PTRAC_FILE or not os.path.isfile(PTRAC_FILE):
    print(f"\n[ERROR] PTRAC_FILE is not set correctly!\n"
          f"Please edit tests/test_eva.py and set PTRAC_FILE to the path of your own PTRAC file.\n"
          f"Current PTRAC_FILE = {PTRAC_FILE}\n")
    exit(1)

# Example MCNPTools code executed inside EVA sandbox
# EVA replaces <PTRAC_PATH_PLACEHOLDER> with the actual PTRAC path
TEST_CODE = """
from mcnptools import Ptrac
from sys import stdout

# Explicitly open the file as binary PTRAC
p = Ptrac(r"<PTRAC_PATH_PLACEHOLDER>", Ptrac.BIN_PTRAC)

# Initialize counter
cnt = 0

# Read histories in batches of 10000
hists = p.ReadHistories(10000)
while hists:
    # Loop over all histories
    for h in hists:
        # Loop over all events in the history
        for e in range(h.GetNumEvents()):
            event = h.GetEvent(e)
            if event.Type() == Ptrac.BNK:
                cnt += 1
                # Print event info (BNK events only)
                stdout.write(
                    "{:13d}{:13.5e}{:13.5e}{:13.5e}{:13.5e}\\n".format(
                        cnt,
                        event.Get(Ptrac.X),
                        event.Get(Ptrac.Y),
                        event.Get(Ptrac.Z),
                        event.Get(Ptrac.ENERGY),
                    )
                )
    hists = p.ReadHistories(10000)

print(f"Total BNK events counted: {cnt}")
"""

class TestEVAAgent(unittest.TestCase):

    def setUp(self):
        # Initialize EVA agent before each test
        self.agent = EVA()

    def test_load_file(self):
        # Ensure EVA can load the PTRAC file
        result = self.agent.load_file(PTRAC_FILE)
        self.assertTrue(result)
        # Last EVA log must confirm file loading
        self.assertIn("[EVA] Fichier PTRAC chargé", self.agent.get_logs()[-1])

    def test_execute_code(self):
        # Load file before executing code
        self.agent.load_file(PTRAC_FILE)
        result = self.agent.execute_code(TEST_CODE)
        # Basic result structure validation
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        self.assertIn("stdout", result)
        self.assertIn("stderr", result)
        self.assertIn("output_files", result)
        # Print debug info for manual inspection
        print("EVA STDOUT:", repr(result["stdout"][:500]))  # show first 500 chars max
        print("EVA STDERR:", repr(result["stderr"]))
        print("EVA EXCEPTION:", repr(result["exception"]))
        # Ensure some output or error was produced
        output_ok = (
            len(result["stdout"].strip()) > 0 or
            len(result["stderr"].strip()) > 0 or
            (result["exception"] is not None and result["exception"] != "Exception")
        )
        self.assertTrue(output_ok, "No useful result or error was produced.")


if __name__ == "__main__":
    unittest.main()
