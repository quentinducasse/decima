
from dotenv import load_dotenv
load_dotenv()
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import re
import unicodedata
from typing import Dict, List, Any

from utils.keywords_quiet import (
    FOCUS_EVENTS,
    FOCUS_DATA,
    FOCUS_DICTIONARIES,
    FOCUS_CLASSES,
    FOCUS_METHODS,
    FOCUS_ATTRIBUTES,
)
from utils.keywords_fr_en import STOPWORDS

def strip_accents(text: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

def simple_plural_forms(word: str):
    forms = {word}
    if word.endswith('s'):
        forms.add(word[:-1])
    else:
        forms.add(word + 's')
    return forms

class QUIET:
    def __init__(self):
        self.focus_events = FOCUS_EVENTS
        self.focus_data = FOCUS_DATA 
        self.focus_dictionaries = FOCUS_DICTIONARIES
        self.focus_classes = [c.upper() for c in FOCUS_CLASSES]
        self.focus_methods = [m.upper() for m in FOCUS_METHODS]
        self.focus_attributes = [a.upper() for a in FOCUS_ATTRIBUTES]
        self.stopwords = STOPWORDS

    def detect_language(self, query: str) -> str:
        french_signals = [
            "combien", "quelle", "quelles", "quels", "particule", "particules",
            "cellule", "cellules", "masse", "poids", "énergie", "durée",
            "événement", "événements", "terminaison", "réactions", "réaction",
            "détecteur", "mesure", "section efficace", "impulsion", "valeur",
            "symbole", "retardé", "fissionnée", "fissionnées", "capturee",
            "capturée", "capturées", "élastique", "élastiques", "inélastique", "inélastiques", "liste"
            "scission", "perdu", "perdus", "cellulaire", "traversant", "fût", "fichier", "trajet", "résultat", "résultats"
        ]
        return "fr" if any(word in query.lower() for word in french_signals) else "en"

    def preprocess_query(self, query: str, lang: str) -> List[str]:
        cleaned = query.lower().replace(";", " ").replace(",", " ")
        words = re.findall(r"\b(?:[A-Za-z]{1,3}-\d{1,3}|\d{1,3}-[A-Za-z]{1,3})\b|\b\w+\b", cleaned)
        # print(f"[QUIET DEBUG] Preprocessed keywords: {words}")
        return [w for w in words if w not in self.stopwords[lang]]

    def _extract_from_map(self, query: str, focus_map: Dict[str, list]) -> List[str]:
        focus = []
        ql = strip_accents(query.lower())
        for fe_key, fe_words in focus_map.items():
            for word in fe_words:
                w_clean = strip_accents(word.lower())
                for var in simple_plural_forms(w_clean):
                    if var in ql:
                        focus.append(fe_key)
                        break
                else:
                    continue
                break
        return sorted(set(focus))

    def extract_focus_events(self, query: str) -> List[str]:
        return self._extract_from_map(query, self.focus_events)

    def extract_focus_data(self, query: str) -> List[str]:
        ql = strip_accents(query.lower())
        found = []
        for k, keywords in self.focus_data.items():
            for word in keywords:
                w_clean = strip_accents(word.lower())
                pattern = r'\b' + re.escape(w_clean) + r'\b'
                if re.search(pattern, ql):
                    found.append(k)
                    break
        return sorted(set(found))


    def extract_focus_dictionaries(self, query: str) -> List[str]:
        ql = strip_accents(query.lower())
        found = []
        for dict_name, dict_words in self.focus_dictionaries.items():
            for word in dict_words:
                w_clean = strip_accents(word.lower())
                for var in simple_plural_forms(w_clean):
                    if var in ql:
                        found.append(dict_name)
                        break
                else:
                    continue
                break
        return sorted(set(found)) if found else [""]

    def extract_focus_classes(self, query: str) -> List[str]:
        ql = strip_accents(query.lower())
        found = []
        for c in self.focus_classes:
            for var in simple_plural_forms(strip_accents(c.lower())):
                if var in ql:
                    found.append(c)
                    break
        return sorted(set(found)) if found else [""]

    def extract_focus_methods(self, query: str) -> List[str]:
        ql = strip_accents(query.lower())
        found = []
        for m in self.focus_methods:
            for var in simple_plural_forms(strip_accents(m.lower())):
                if var in ql:
                    found.append(m)
                    break
        return sorted(set(found)) if found else [""]

    def extract_focus_attributes(self, query: str) -> List[str]:
        ql = strip_accents(query.lower())
        found = []
        for a in self.focus_attributes:
            for var in simple_plural_forms(strip_accents(a.lower())):
                if var in ql:
                    found.append(a)
                    break
        return sorted(set(found)) if found else [""]

    def analyze(self, query: str) -> Dict[str, Any]:
        lang = self.detect_language(query)
        keywords = self.preprocess_query(query, lang)
        res = {
            "query": query,
            "language": lang,
            "focus_events": self.extract_focus_events(query),
            "focus_data": self.extract_focus_data(query),
            "focus_dictionaries": self.extract_focus_dictionaries(query),
            "focus_classes": self.extract_focus_classes(query),
            "focus_methods": self.extract_focus_methods(query),
            "focus_attributes": self.extract_focus_attributes(query),
            "Query entities of interest": [k.upper() for k in keywords if len(k) > 2],
        }
        return res

if __name__ == "__main__":
    qagent = QUIET()
    test_query = "Affiche la position (x, y, z) et l'énergie des événements de banque."
    result = qagent.analyze(test_query)
    from pprint import pprint
    pprint(result)
