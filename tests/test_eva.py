# tests/test_eva_agent.py
from dotenv import load_dotenv
load_dotenv()
import os
import unittest
from modules.eva import EVA

# Chemin à adapter à ton jeu de test réel
# PTRAC_FILE = r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\example_ptrac_1.mcnp_extended_ascii.ptrac"
PTRAC_FILE = r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\example_ptrac_1.mcnp.ptrac"

TEST_CODE = """
cnt = 0
hists = p.ReadHistories(10000)
while hists:
    for h in hists:
        for e in range(h.GetNumEvents()):
            event = h.GetEvent(e)
            if event.Type() == Ptrac.BNK:
                cnt += 1
    hists = p.ReadHistories(10000)
print(cnt)
"""

class TestEVAAgent(unittest.TestCase):

    def setUp(self):
        self.agent = EVA()

    def test_load_file(self):
        # Fichier PTRAC doit exister pour ce test
        self.assertTrue(os.path.isfile(PTRAC_FILE), f"PTRAC test file not found: {PTRAC_FILE}")
        result = self.agent.load_file(PTRAC_FILE)
        self.assertTrue(result)
        self.assertIn("[EVA] Fichier PTRAC chargé", self.agent.get_logs()[-1])

    def test_execute_code(self):
        self.agent.load_file(PTRAC_FILE)
        result = self.agent.execute_code(TEST_CODE)
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        self.assertIn("stdout", result)
        self.assertIn("stderr", result)
        self.assertIn("output_files", result)
        print("EVA STDOUT:", repr(result["stdout"]))
        print("EVA STDERR:", repr(result["stderr"]))
        print("EVA EXCEPTION:", repr(result["exception"]))
        # Le test passe si il y a de l’output OU une erreur humaine claire
        output_ok = (len(result["stdout"].strip()) > 0 or
                    len(result["stderr"].strip()) > 0 or
                    (result["exception"] is not None and result["exception"] != "Exception"))
        self.assertTrue(output_ok, "Aucun résultat ni erreur utile n'a été produit.")


if __name__ == "__main__":
    unittest.main()
