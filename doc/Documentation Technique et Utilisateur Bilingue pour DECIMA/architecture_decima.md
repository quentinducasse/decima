# DECIMA – Architecture du projet (v2)

Ce fichier documente l'architecture du projet **DECIMA v2**, en se basant sur les dossiers utiles et les fichiers pertinents (code source, contextes, scripts, interfaces). Il exclut les dossiers temporaires ou d'environnement (`decima_env`, `.vscode`, `__pycache__`).

---

## 📁 Racine du projet (`.`)

| Fichier / dossier | Description |
|-------------------|-------------|
| `app.py` | Point d'entrée principal de l'application (ex: interface ou test orchestrateur) |
| `tree_filtered.py` | Script pour afficher l'arborescence filtrée du projet |

---

## 📁 `data/`
Fichiers C++ et exemples d'utilisation MCNP.

### C++ source et headers
- `cpp/` : implémentations C++ (ex: `Ptrac.cpp`, `Mctal.cpp`)
- `hpp/` : headers (notamment `PtracEnums.hpp`, `Ptrac.hpp`, etc.)
- `mctal/` : spécifique à l'analyse MCTAL

### Fichiers MCNP et scripts associés
- `mcnp_files/`, `mctal_samples/`, `ptrac_samples/` : exemples de fichiers d'entrée/sortie
- `mctal_scripts/`, `ptrac_scripts/` : scripts Python/C++ de démonstration ou test (e.g. `python_example_ptrac_1.py`, `test_ptrac_decima.py`)

---

## 📁 `doc/`
Dossier réservé à la documentation utilisateur ou développeur (contenu non listé ici).

---

## 📁 `frontend/`
Interface web HTML/JS statique (si utilisée).

| Fichier / dossier | Description |
|-------------------|-------------|
| `index.html` | Page d'accueil de l'interface (frontend) |
| `static/css`, `static/js` | Dossiers pour les styles et scripts |

---

## 📁 `kg/`
Backend du Knowledge Graph (Neo4j).

- `loader/neo4j_loader.py` : loader principal (import de triplets)
- `triplets/` : fichiers JSON décrivant le graphe (par classe, enums, relations...)
- `__init__.py` : permet de traiter `kg/` comme package Python

---

## 📁 `modules/`
Modules fonctionnels (anciennement "agents") du POC DECIMA.

| Fichier | Rôle |
|--------|-------|
| `campbell.py` | Orchestrateur principal du workflow (LangGraph) |
| `quiet.py` | Analyse préliminaire de la requête (détection d'entités, routage) |
| `emma.py` | Accès et extraction de contexte depuis le Knowledge Graph (EMMA) |
| `otacon.py` | Génération de code/explication via LLM (OTACON) |
| `eva.py` | Exécution du code sur fichier PTRAC (EVA) |

---

## 📁 `tests/`
Tests unitaires et d'intégration.

| Fichier | Teste quoi ? |
|---------|--------------|
| `test_campbell_workflow.py` | Exécution complète du pipeline DECIMA |
| `test_emma.py`, `test_quiet.py`, ... | Modules spécifiques |
| `testsets/` | Jeux de tests JSON pour l'évaluation des entités (e.g. `matching_eval_BNK_ZAID.json`) |

---

## 📁 `tools/`
Outils internes ou d’exécution.

- `sandbox.py` : exécution sécurisée du code Python sur fichier PTRAC (utilisé par EVA)

---

## 📁 `uploads/`
Dossier réservé aux fichiers temporairement téléversés (ex: interface web)

---

## 📁 `utils/`
Fichiers de support pour le NLP et le contexte LLM.

| Fichier | Contenu |
|---------|---------|
| `keywords_fr_en.py` | Lexique bilingue FR/EN pour le traitement de requêtes |
| `keywords_quiet.py` | Mapping de dicos/classes/méthodes ciblés par QUIET |

### `llm_basic_context/`
Contexte statique injecté pour OTACON :
- `kg_context_code_structure.py` : structure des classes/méthodes MCNPTools
- `kg_context_example_code.py` : exemple de code complet utilisé comme démo pour LLM

---

## 🔍 En bref : composants clés

| Composant | Rôle principal |
|-----------|-----------------|
| QUIET     | Analyse de requête, extraction des focus |
| EMMA      | Extraction contextuelle depuis KG (Neo4j) |
| OTACON    | Réponse et code via LLM |
| EVA       | Exécution réelle du code sur PTRAC |
| CAMPBELL  | Orchestration du pipeline |

---

## 📁 Arborescence filtrée du projet

```
.
  └── app.py
  └── tree_filtered.py
data
  cpp
    └── Ptrac.cpp
    └── PtracEvent.cpp
    └── PtracHistory.cpp
    └── PtracNps.cpp
    mctal
      └── Mctal.cpp
      └── MctalTally.cpp
  hpp
    └── Ptrac.hpp
    └── PtracEnums.hpp
    └── PtracEvent.hpp
    └── PtracHistory.hpp
    └── PtracNps.hpp
    mctal
      └── Mctal.hpp
      └── MctalTally.hpp
  mcnp_files
  mctal_samples
  mctal_scripts
    └── cpp_example_mctal_1.cpp
    └── python_example_mctal_1.py
  ptrac_samples
  ptrac_scripts
    └── cpp_example_ptrac_1.cpp
    └── ptrac_wrap.py
    └── python_example_ptrac_1.py
    └── python_example_ptrac_1_decima.py
    └── python_example_ptrac_ascii.py
    └── python_example_ptrac_walkthrough.py
    └── test_ptrac_decima.py
doc
frontend
  └── index.html
  pics
  static
    css
    js
kg
  └── __init__.py
  loader
    └── neo4j_loader.py
  triplets
    └── kg_ptrac_class.json
    └── kg_ptrac_class_relations.json
    └── kg_ptrac_enums_banktypes.json
    └── kg_ptrac_enums_class.json
    └── kg_ptrac_enums_datatypes.json
    └── kg_ptrac_enums_eventtypes.json
    └── kg_ptrac_enums_formats.json
    └── kg_ptrac_enums_particletypes.json
    └── kg_ptrac_enums_reactiontypes.json
    └── kg_ptrac_enums_terminationtypes.json
    └── kg_ptrac_enums_zaids.json
    └── kg_ptrac_event_class.json
    └── kg_ptrac_history_class.json
    └── kg_ptrac_nps_class.json
modules
  └── campbell.py
  └── emma.py
  └── eva.py
  └── otacon.py
  └── quiet.py
tests
  └── test_campbell_workflow.py
  └── test_decima_01.py
  └── test_emma.py
  └── test_eva.py
  └── test_otacon_api.py
  └── test_quiet.py
  testsets
    └── matching_eval.json
    └── matching_eval_48queries.json
    └── matching_eval_BNK_ZAID.json
    └── matching_eval_TER.json
    └── matching_eval_particle.json
    └── matching_eval_reactions.json
tools
  └── sandbox.py
uploads
utils
  └── keywords_fr_en.py
  └── keywords_quiet.py
  llm_basic_context
    └── kg_context_code_structure.py
    └── kg_context_example_code.py
```

> Dernière mise à jour : 2025-07-16

