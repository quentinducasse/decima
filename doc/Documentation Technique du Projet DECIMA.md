# Documentation Technique du Projet DECIMA

**Auteur :** DECIMA Team

**Date :** 1er Sept 2025

## 1. Introduction

Le projet DECIMA (Data Extraction & Contextual Inference for MCNP Analysis) est une solution avancée conçue pour faciliter l'analyse et l'interprétation des fichiers de trajectoires de particules (PTRAC) générés par le code de transport de Monte Carlo MCNP. Il vise à transformer des requêtes utilisateur en langage naturel en des analyses de données complexes, en générant et exécutant du code Python via la bibliothèque `mcnptools`. DECIMA se positionne comme un assistant intelligent pour les ingénieurs et chercheurs manipulant des données de simulation nucléaire, en automatisant des tâches d'extraction et de traitement qui seraient autrement fastidieuses et sujettes aux erreurs manuelles.

L'objectif principal de DECIMA est de démocratiser l'accès aux informations contenues dans les fichiers PTRAC, en permettant aux utilisateurs de poser des questions intuitives sans nécessiter une expertise approfondie en programmation ou en structure interne des fichiers PTRAC. Le système orchestre plusieurs modules spécialisés, chacun contribuant à une étape clé du processus, de la compréhension de la requête à l'exécution du code et à la présentation des résultats.

Ce document fournit une vue d'ensemble technique détaillée de l'architecture de DECIMA, de ses composants logiciels, de leurs interactions, et des technologies sous-jacentes. Il est destiné aux développeurs, aux architectes logiciels et à toute personne souhaitant comprendre le fonctionnement interne du système pour des raisons de maintenance, d'extension ou de débogage.




## 2. Architecture Globale

L'architecture de DECIMA est modulaire et s'appuie sur une approche basée sur des agents, orchestrés par un composant central. Cette conception permet une grande flexibilité, une maintenabilité accrue et la possibilité d'intégrer de nouvelles fonctionnalités ou de remplacer des modules existants sans affecter l'ensemble du système. Le cœur de l'orchestration est géré par LangGraph, une bibliothèque qui facilite la construction de graphes d'états pour des workflows complexes basés sur des modèles de langage.

Le système est structuré autour de plusieurs modules principaux, chacun ayant une responsabilité bien définie :

*   **QUIET (Analyse de Requête) :** Responsable de la détection de la langue, de l'extraction des mots-clés et des entités pertinentes à partir de la requête utilisateur. Il prépare la requête pour les étapes suivantes en identifiant les focus (événements, données, classes, méthodes, attributs) et les intentions de l'utilisateur.
*   **EMMA (Extraction Contextuelle du Knowledge Graph) :** Interagit avec une base de données Neo4j (Knowledge Graph) pour enrichir la requête avec des informations contextuelles. Il utilise les entités identifiées par QUIET pour récupérer des détails sur les classes `mcnptools`, les énumérations, les dictionnaires et les relations, fournissant ainsi un contexte sémantique riche pour le LLM.
*   **OTACON (Génération de Réponse et de Code) :** Le module central basé sur un Grand Modèle de Langage (LLM). Il reçoit la requête utilisateur enrichie par le contexte d'EMMA et génère une explication en langage naturel ainsi que le code Python correspondant. OTACON est entraîné pour produire du code `mcnptools` précis et pertinent pour l'analyse des fichiers PTRAC.
*   **EVA (Exécution et Validation) :** Exécute le code Python généré par OTACON dans un environnement sandboxisé. Il gère le chargement du fichier PTRAC, l'exécution sécurisée du code, la capture des sorties (stdout, stderr), et la gestion des erreurs. EVA est crucial pour garantir la sécurité et la fiabilité de l'exécution du code généré par le LLM.
*   **CAMPBELL (Orchestrateur Principal) :** Le chef d'orchestre du système. Il coordonne le flux d'informations entre QUIET, EMMA, OTACON et EVA, en gérant les transitions d'état et en s'assurant que chaque module reçoit les entrées appropriées et produit les sorties attendues. CAMPBELL est implémenté avec LangGraph pour une gestion robuste du workflow.

En plus de ces modules principaux, DECIMA intègre une interface utilisateur web (frontend) basée sur Flask, HTML, CSS et JavaScript, permettant aux utilisateurs d'interagir avec le système de manière intuitive. Un dossier `uploads` est dédié à la gestion temporaire des fichiers PTRAC téléchargés par l'utilisateur. Des utilitaires (`utils`) et des scripts de test (`tests`) complètent l'écosystème du projet.

L'interaction entre ces composants suit un pipeline séquentiel : la requête utilisateur est d'abord analysée, puis enrichie par le contexte, le code est généré, et enfin exécuté. Les résultats de l'exécution sont ensuite présentés à l'utilisateur via l'interface web. Cette architecture garantit une séparation claire des préoccupations et une grande scalabilité pour les futures évolutions du projet.




## 3. Composants Détaillés

Cette section décrit en détail le rôle, les fonctionnalités et les interactions de chaque module clé de DECIMA.

### 3.1. QUIET (Analyse Préliminaire de la Requête)

**Fichier :** `modules/quiet.py`

Le module QUIET est la première étape du pipeline de traitement d'une requête utilisateur. Son rôle est d'analyser la requête en langage naturel pour en extraire des informations structurées qui guideront les modules suivants. Il effectue une détection de la langue, une tokenisation, une normalisation et une extraction d'entités clés.

**Fonctionnalités principales :**

*   **Détection de la langue (`detect_language`) :** Identifie si la requête est en français ou en anglais en se basant sur un ensemble de mots-clés spécifiques à chaque langue. Cela permet d'adapter le traitement ultérieur, notamment l'utilisation des *stopwords* et du lexique bilingue.
*   **Prétraitement de la requête (`preprocess_query`) :** Convertit la requête en minuscules, supprime la ponctuation et les *stopwords* (mots vides) spécifiques à la langue détectée. Il gère également l'extraction de mots-clés complexes comme les identifiants MCNP (ex: `MT-101`).
*   **Extraction des focus (`extract_focus_events`, `extract_focus_data`, etc.) :** C'est la fonction la plus critique de QUIET. Elle utilise des dictionnaires de mots-clés (`FOCUS_EVENTS`, `FOCUS_DATA`, `FOCUS_DICTIONARIES`, `FOCUS_CLASSES`, `FOCUS_METHODS`, `FOCUS_ATTRIBUTES`) pour identifier les concepts métiers pertinents mentionnés dans la requête. Ces dictionnaires sont définis dans `utils/keywords_quiet.py` et `utils/keywords_fr_en.py`. L'extraction prend en compte les formes plurielles et singulières, ainsi que les accents, pour une robustesse accrue.
    *   `FOCUS_EVENTS` : Identifie les types d'événements PTRAC (Source, Bank, Collision, Termination, Surface, Lost).
    *   `FOCUS_DATA` : Détecte les champs de données PTRAC (NPS, Energy, Time, X, Y, Z, Particle, Cell, Surface, Tally, etc.).
    *   `FOCUS_DICTIONARIES` : Reconnaît les références aux dictionnaires du Knowledge Graph (ParticleCodeDict, PtracZAIDDict, PtracReactionDict).
    *   `FOCUS_CLASSES`, `FOCUS_METHODS`, `FOCUS_ATTRIBUTES` : Identifie les classes, méthodes et attributs de la bibliothèque `mcnptools` mentionnés dans la requête.

**Sortie :** Le module QUIET retourne un dictionnaire contenant la requête originale, la langue détectée, et des listes d'entités identifiées pour chaque catégorie de focus. Ce dictionnaire est ensuite passé à EMMA pour l'enrichissement contextuel.

**Exemple de fonctionnement :**
Si la requête est : *"Quelle est la position x, y, z et l'énergie des neutrons qui traversent la surface 300 ?"*
QUIET va détecter :
*   `language`: `fr`
*   `focus_data`: `['X', 'Y', 'Z', 'ENERGY', 'PARTICLE', 'SURFACE']`
*   `focus_dictionaries`: `['ParticleCodeDict']` (pour 'neutrons')
*   `focus_events`: `['SUR']` (pour 'traversent la surface')

Ces informations structurées sont essentielles pour qu'EMMA puisse interroger le Knowledge Graph de manière pertinente et qu'OTACON puisse générer le code Python adéquat.

### 3.2. EMMA (Extraction Contextuelle du Knowledge Graph)

**Fichier :** `modules/emma.py`

Le module EMMA est responsable de l'extraction de contexte pertinent à partir du Knowledge Graph (KG) basé sur Neo4j. Il utilise les informations structurées fournies par QUIET pour interroger le KG et récupérer des détails sur les entités (classes, énumérations, méthodes, attributs, valeurs de dictionnaires) qui correspondent à la requête de l'utilisateur. L'objectif est de fournir à OTACON un contexte sémantique riche et précis, réduisant ainsi les risques d'hallucinations ou d'erreurs dans le code généré.

**Fonctionnalités principales :**

*   **Connexion à Neo4j :** EMMA se connecte à une instance Neo4j en utilisant les informations d'authentification définies dans les variables d'environnement. Le `neo4j_loader.py` est utilisé pour gérer cette connexion et les opérations de base sur le graphe.
*   **Extraction d'entités (`extract_kg_context`) :** C'est la fonction centrale d'EMMA. Elle prend en entrée le dictionnaire de focus généré par QUIET et effectue des requêtes Cypher sur le KG. Pour chaque type de focus (événements, données, dictionnaires, classes, méthodes, attributs), EMMA recherche les nœuds correspondants dans le graphe.
*   **Gestion des dictionnaires spécifiques (MT, Particle, ZAID) :** EMMA implémente une logique de scoring avancée pour les dictionnaires `PtracReactionDict` (MT_xxx), `ParticleCodeDict` et `PtracZAIDDict`. Cela permet de classer les entités les plus pertinentes en fonction de la requête, en prenant en compte :
    *   Les numéros MT explicites (ex: `MT_101`).
    *   Les particules mentionnées (ex: `neutron`, `photon`).
    *   Les motifs de réaction (ex: `(n,p)`, `n,3a`).
    *   Les mots-clés généraux (ex: `fission`, `capture`).
    Cette approche discriminante assure que seules les entités les plus pertinentes sont transmises à OTACON, évitant ainsi un "bruit" excessif dans le contexte.
*   **Enrichissement des entités :** Pour chaque entité trouvée dans le KG, EMMA récupère des informations complètes telles que son type, sa description, sa classe parente, son énumération parente, et son dictionnaire parent. Ces informations sont cruciales pour OTACON afin de comprendre la sémantique des entités et de générer du code correct.
*   **Normalisation et lexique :** EMMA utilise le lexique bilingue (`FR_TO_EN_LEXICON` dans `utils/keywords_fr_en.py`) pour normaliser les mots-clés et s'assurer que les requêtes au KG sont cohérentes, quelle que soit la langue d'origine de la requête utilisateur.

**Sortie :** EMMA retourne un dictionnaire `emma_context` qui contient une liste d'entités enrichies. Chaque entité est un dictionnaire avec des champs comme `id`, `type`, `description`, `parent_class`, `parent_enum`, `parent_dict`, et un `score` indiquant sa pertinence. Ce contexte est directement injecté dans le prompt d'OTACON.

### 3.3. OTACON (Génération de Réponse et de Code)

**Fichier :** `modules/otacon.py`

OTACON est le cerveau de DECIMA, un agent basé sur un Grand Modèle de Langage (LLM) qui transforme la requête utilisateur et le contexte EMMA en une explication en langage naturel et en code Python exécutable. Il est conçu pour être un expert en analyse de fichiers PTRAC MCNP et en utilisation de la bibliothèque `mcnptools`.

**Fonctionnalités principales :**

*   **Construction du prompt (`build_prompt`) :** OTACON construit un prompt détaillé pour le LLM en combinant plusieurs sources d'information :
    *   **Instructions système :** Définit le rôle d'OTACON (expert MCNP PTRAC), ses limites (répondre uniquement aux requêtes PTRAC, utiliser `mcnptools`), et le format de sortie attendu (explication + bloc de code Python).
    *   **Contexte EMMA :** La liste des entités pertinentes extraites par EMMA est insérée directement dans le prompt. OTACON est instruit d'utiliser ce contexte comme un guide, mais de ne pas le considérer comme une vérité absolue, lui permettant de s'appuyer sur son propre savoir ou le contexte large structuré si EMMA est incomplet ou erroné.
    *   **Contexte large structuré (`KG_CONTEXT_CODE_STRUCTURE`) :** Une description exhaustive et fiable des classes, méthodes, énumérations et structures de `mcnptools` est fournie. Cela inclut la signature des méthodes, les types de retour, et les relations entre les classes. Ce contexte est crucial pour garantir la génération de code syntaxiquement et sémantiquement correct.
    *   **Exemple de code (`KG_CONTEXT_EXAMPLE_CODE`) :** Un exemple complet d'analyse PTRAC avec `mcnptools` est inclus pour guider le LLM sur les bonnes pratiques de codage et la structure générale du script Python.
    *   **Règles et bonnes pratiques (`KG_CONTEXT_RULES`) :** Des règles strictes sont imposées au LLM, telles que l'interdiction d'importer des classes `mcnptools` autres que `Ptrac`, l'obligation d'utiliser les méthodes publiques plutôt que les attributs internes, et l'utilisation d'un placeholder pour le chemin du fichier PTRAC (`<PTRAC_PATH_PLACEHOLDER>`). Des bonnes pratiques sur le traçage des particules et le calcul des grandeurs physiques (énergie déposée, temps de vol) sont également fournies pour éviter les erreurs courantes.
    *   **Requête utilisateur :** La requête originale de l'utilisateur est ajoutée à la fin du prompt.
*   **Appel au LLM (`ask_llm`) :** OTACON utilise l'API OpenAI (ou un modèle compatible) pour interroger le LLM avec le prompt construit. La température est réglée à 0.2 pour favoriser des réponses plus déterministes et moins créatives, ce qui est souhaitable pour la génération de code technique.
*   **Parsing de la sortie LLM (`parse_llm_output`) :** La réponse brute du LLM est analysée pour séparer l'explication en langage naturel du bloc de code Python. Le code est extrait s'il est encadré par des balises ```python...```.

**Sortie :** OTACON retourne un dictionnaire contenant l'explication générée par le LLM, le code Python extrait, et la sortie brute du LLM pour le débogage. Le code Python est ensuite transmis à EVA pour exécution.

### 3.4. EVA (Exécution et Validation du Code)

**Fichier :** `modules/eva.py` et `tools/sandbox.py`

EVA est le module chargé d'exécuter le code Python généré par OTACON dans un environnement sécurisé et de capturer les résultats. Il s'appuie sur le module `sandbox.py` pour l'isolation et la gestion de l'exécution.

**Fonctionnalités principales :**

*   **Chargement du fichier PTRAC (`load_file`) :** Prend en paramètre le chemin d'accès au fichier PTRAC que l'utilisateur a téléchargé. Il vérifie l'existence du fichier et le rend disponible pour l'exécution du code.
*   **Exécution sécurisée du code (`execute_code`) :** C'est la fonction clé d'EVA, qui délègue la majeure partie du travail à `run_ptrac_code` dans `tools/sandbox.py`.
    *   **Substitution du chemin PTRAC :** Le placeholder `<PTRAC_PATH_PLACEHOLDER>` dans le code généré par OTACON est remplacé par le chemin réel du fichier PTRAC chargé par l'utilisateur.
    *   **Détection du mode PTRAC :** Avant l'exécution, `sandbox.py` détecte automatiquement si le fichier PTRAC est binaire (`BIN_PTRAC`) ou ASCII (`ASC_PTRAC`) et adapte l'instanciation de l'objet `Ptrac` en conséquence. Cela garantit la compatibilité avec différents formats de fichiers MCNP.
    *   **Patching du code :** `sandbox.py` effectue des modifications sur le code généré pour :
        *   S'assurer que toutes les instanciations de `Ptrac` utilisent le mode détecté (`patch_ptrac_instantiation`).
        *   Désactiver les fonctions de plotting (`plt.show()`, `plt.savefig()`, etc.) si `allow_plots` est `False`, pour éviter les interactions graphiques non désirées dans l'environnement sandboxisé (`patch_disable_plots`).
    *   **Exécution en sandbox :** Le code est écrit dans un fichier temporaire et exécuté dans un sous-processus Python isolé. Cela empêche le code généré d'accéder au système de fichiers hôte ou d'exécuter des opérations dangereuses. Un timeout est appliqué pour éviter les boucles infinies ou les exécutions trop longues.
    *   **Capture des sorties :** `stdout` (sortie standard) et `stderr` (erreurs standard) du processus sandboxisé sont capturés. Toute exception levée pendant l'exécution est également enregistrée.
    *   **Gestion de l'interruption :** Le module `sandbox.py` gère un processus actif (`ACTIVE_PROCESS`) qui peut être terminé manuellement via l'API `/abort_execution` de l'application Flask, permettant à l'utilisateur d'arrêter une exécution de code bloquée.

**Sortie :** EVA retourne un dictionnaire contenant `success` (booléen indiquant si l'exécution a réussi), `stdout`, `stderr`, `exception` (le cas échéant), et `output_files` (pour les fichiers générés, bien que non pleinement exploité pour l'instant pour les plots).

### 3.5. CAMPBELL (Orchestrateur Principal)

**Fichier :** `modules/campbell.py`

CAMPBELL est le module central de DECIMA, agissant comme l'orchestrateur principal du workflow. Il est construit en utilisant la bibliothèque LangGraph, ce qui lui permet de définir un graphe d'états pour gérer la séquence d'appels entre QUIET, EMMA, OTACON et EVA. Cette approche basée sur un graphe offre une grande flexibilité pour les workflows complexes et conditionnels.

**Fonctionnalités principales :**

*   **Définition de l'état (`AgentState`) :** CAMPBELL définit une structure `TypedDict` (`AgentState`) qui représente l'état global du workflow. Cet état contient toutes les informations pertinentes qui sont passées d'un module à l'autre, telles que la requête utilisateur, la langue, les focus extraits, le contexte EMMA, la réponse du LLM, le code généré, le chemin du fichier PTRAC, et les résultats d'exécution.
*   **Création du workflow (`_create_workflow`) :** Utilise `StateGraph` de LangGraph pour définir les nœuds (chaque module est un nœud) et les transitions entre eux. Le workflow est séquentiel mais inclut une transition conditionnelle après OTACON :
    *   `quiet` -> `emma`
    *   `emma` -> `otacon`
    *   `otacon` -> `eva` (si du code a été généré et un fichier PTRAC est fourni)
    *   `otacon` -> `END` (si aucun code n'a été généré ou aucun fichier PTRAC n'est fourni)
    *   `eva` -> `END`
*   **Nœuds du workflow (`_run_quiet_agent`, `_run_emma_agent`, etc.) :** Chaque méthode encapsule l'appel à un module spécifique (QUIET, EMMA, OTACON, EVA) et met à jour l'état global du workflow avec les résultats de l'exécution du module. La gestion des erreurs est intégrée à chaque nœud, permettant de capturer les exceptions et de mettre à jour le statut du workflow en conséquence.
*   **Transition conditionnelle (`_route_after_otacon`) :** Cette fonction de routage détermine si le workflow doit passer à EVA (pour exécuter le code) ou se terminer directement après OTACON. Cette décision est basée sur la présence de code généré par OTACON et la disponibilité d'un fichier PTRAC.
*   **API principale (`process_query`) :** La méthode `process_query` est le point d'entrée public de CAMPBELL. Elle initialise l'état du workflow avec la requête utilisateur et le chemin du fichier PTRAC, puis invoque le graphe d'états de LangGraph. Elle retourne l'état final du workflow, contenant toutes les informations générées par les différents modules.

**Interactions avec l'application Flask (`app.py`) :** CAMPBELL est instancié une fois au démarrage de l'application Flask. Les routes `/analyze_query` et `/execute_code` de l'application Flask appellent respectivement `campbell.process_query` et `eva.execute_code` (via une instanciation directe d'EVA pour l'exécution manuelle du code). Cela permet à l'interface web de déclencher le workflow DECIMA et de récupérer les résultats.




### 3.6. Frontend (Interface Utilisateur)

**Fichiers :** `frontend/index.html`, `frontend/static/js/main.js`, `frontend/static/css/style.css`

L'interface utilisateur de DECIMA est une application web simple et intuitive, construite avec Flask pour le backend et des technologies web standards (HTML, CSS, JavaScript) pour le frontend. Elle permet aux utilisateurs de télécharger des fichiers PTRAC, de soumettre des requêtes en langage naturel et de visualiser les réponses du LLM ainsi que les résultats de l'exécution du code.

**Composants clés :**

*   **`index.html` :** Le fichier HTML principal qui définit la structure de la page. Il inclut des liens vers les feuilles de style CSS et les scripts JavaScript, et contient les éléments de l'interface utilisateur tels que le bouton de téléchargement de fichier, le champ de saisie de la requête, la zone d'affichage des messages de chat, et les blocs pour les résultats d'exécution du code.
*   **`style.css` :** La feuille de style CSS qui gère l'apparence visuelle de l'application. Elle définit les couleurs, les polices, les mises en page (flexbox pour l'organisation des sections), et les styles des différents éléments de l'interface pour une expérience utilisateur agréable et cohérente avec l'identité visuelle de DECIMA.
*   **`main.js` :** Le script JavaScript qui gère l'interactivité du frontend. Ses fonctionnalités principales incluent :
    *   **Téléchargement de fichier PTRAC :** Gère la sélection et l'envoi du fichier PTRAC au backend via une requête `POST` vers l'endpoint `/data/ptrac_samples`. Il met à jour l'interface pour afficher le nom du fichier chargé.
    *   **Envoi de requêtes :** Capture la requête saisie par l'utilisateur et l'envoie au backend via une requête `POST` vers l'endpoint `/analyze_query`. Il affiche la requête de l'utilisateur dans la zone de chat et active un indicateur de chargement (`reasoning-loader`).
    *   **Affichage des réponses du LLM :** Reçoit la réponse du backend (explication et code Python) et l'affiche dans la zone de chat. Le code Python est formaté avec `highlight.js` pour une meilleure lisibilité.
    *   **Exécution du code généré :** Un bouton "Exécuter le code" est ajouté dynamiquement sous le bloc de code Python. Lorsque l'utilisateur clique dessus, le code est envoyé au backend via une requête `POST` vers l'endpoint `/execute_code`. Le script gère également l'affichage des sorties `stdout`, `stderr` et des éventuels fichiers de sortie (comme des images de plots) dans la section des résultats.
    *   **Gestion de l'interruption :** Un bouton "Stop Code Generation" est implémenté pour permettre à l'utilisateur d'interrompre l'exécution d'un code long ou bloqué via l'endpoint `/abort_execution`.
    *   **Gestion du contexte :** Une case à cocher "Add context" permet à l'utilisateur de choisir si le contexte EMMA doit être utilisé ou non lors de l'analyse de la requête par OTACON.

L'interface est conçue pour être réactive et offrir une expérience utilisateur fluide, avec des indicateurs visuels pour les opérations en cours et une mise en forme claire des informations.

### 3.7. Knowledge Graph (Neo4j)

**Fichiers :** `kg/loader/neo4j_loader.py`, `kg/triplets/*.json`

Le Knowledge Graph (KG) est une composante fondamentale de DECIMA, fournissant une représentation structurée des connaissances relatives à la bibliothèque `mcnptools` et aux concepts MCNP/PTRAC. Il est implémenté en utilisant Neo4j, une base de données de graphes, ce qui permet de modéliser efficacement les relations complexes entre les entités.

**Structure du KG :**

Le KG est peuplé à partir de fichiers JSON (`kg/triplets/*.json`) qui décrivent des triplets (Sujet, Prédicat, Objet). Ces triplets représentent des entités (nœuds) et les relations (arêtes) entre elles. Les types d'entités incluent :

*   **Classes :** Représentent les classes Python de `mcnptools` (ex: `Ptrac`, `PtracEvent`, `PtracHistory`).
*   **Enums :** Représentent les énumérations MCNP (ex: `PtracEventType`, `PtracBankType`, `PtracDataType`).
*   **EnumValues :** Représentent les valeurs spécifiques au sein des énumérations (ex: `SRC`, `BNK`, `TER` pour `PtracEventType`).
*   **Methods :** Représentent les méthodes des classes `mcnptools` (ex: `GetNPS()`, `Has(DATA)`).
*   **Attributes :** Représentent les attributs des classes.
*   **Dictionaries :** Représentent des dictionnaires de mapping (ex: `ParticleCodeDict`, `PtracReactionDict`, `PtracZAIDDict`).
*   **ParticleCode, ReactionCode, ZAIDCode :** Représentent des codes spécifiques (particules, réactions, ZAID) et leurs descriptions.

Les relations entre ces entités incluent `HAS_ENUM`, `BELONGS_TO_ENUM`, `IS_METHOD_OF`, `HAS_ATTRIBUTE`, `BELONGS_TO_DICT`, etc., permettant de naviguer et d'interroger le graphe pour extraire des informations contextuelles.

**`neo4j_loader.py` :** Ce script est responsable de la migration des données des fichiers JSON de triplets vers la base de données Neo4j. Il effectue les opérations suivantes :

*   **Connexion :** Établit une connexion avec l'instance Neo4j.
*   **Suppression des données existantes :** Au début de chaque migration, toutes les données existantes dans le graphe sont supprimées pour assurer une base propre.
*   **Création de contraintes :** Définit des contraintes d'unicité sur les noms des nœuds pour garantir l'intégrité des données et optimiser les requêtes.
*   **Création des nœuds :** Parcourt tous les triplets pour identifier les sujets et objets, et crée les nœuds correspondants dans le graphe avec les labels appropriés (Class, Enum, EnumValue, etc.).
*   **Ajout de propriétés :** Ajoute les propriétés (description, valeur, etc.) aux nœuds.
*   **Création des relations :** Établit les relations entre les nœuds en se basant sur les prédicats des triplets. Une logique spécifique est appliquée pour certains prédicats (`has_enum`, `belongs_to_enum`) afin d'assurer la cohérence des labels.

Le KG est une ressource essentielle pour EMMA, lui permettant de fournir à OTACON un contexte sémantique précis et pertinent, ce qui est crucial pour la génération de code et de réponses de haute qualité.




## 4. La Bibliothèque `mcnptools`

La bibliothèque `mcnptools` est au cœur du projet DECIMA, servant de fondation pour l'analyse des fichiers PTRAC. C'est une bibliothèque Python (avec des composants C++ sous-jacents pour la performance) conçue spécifiquement pour la lecture, le parsing et la manipulation des données de sortie des simulations MCNP, en particulier les fichiers PTRAC (Particle Track). Elle offre une interface programmatique pour accéder aux informations détaillées sur les trajectoires des particules, les événements de collision, les banques, les terminaisons, et d'autres données pertinentes.

**Concepts Clés de `mcnptools` :**

*   **`Ptrac` :** La classe principale pour interagir avec un fichier PTRAC. Elle permet d'ouvrir le fichier, de lire son en-tête et de récupérer les histoires de particules (`PtracHistory`). Elle gère également les différents formats de fichiers PTRAC (binaire, ASCII).
*   **`PtracHistory` :** Représente une seule histoire de particule (ou trajectoire) dans le fichier PTRAC. Une histoire est une séquence d'événements qui décrivent le parcours d'une particule et de ses secondaires générées au cours d'une simulation. Cette classe fournit des méthodes pour accéder au nombre d'événements dans l'histoire et pour récupérer des événements individuels (`PtracEvent`).
*   **`PtracEvent` :** Représente un événement unique dans une histoire de particule. Un événement peut être une source (SRC), une banque (BNK), une collision (COL), une traversée de surface (SUR), une terminaison (TER), ou une perte (LST). Chaque événement contient des données spécifiques (position, énergie, temps, type de particule, etc.) qui peuvent être accédées via des méthodes génériques (`Has`, `Get`).
*   **`PtracNps` :** Contient des informations récapitulatives sur une histoire de particule, telles que le nombre de particules simulées (NPS), la cellule, la surface, le tally associé, et une valeur générale. Cette classe est souvent utilisée pour des analyses agrégées ou pour filtrer les histoires.
*   **Énumérations (`PtracEnums`) :** `mcnptools` utilise des énumérations pour représenter des types d'événements (`PtracEventType`), des types de banques (`PtracBankType`), des types de terminaisons (`PtracTerminationType`), et des types de données (`PtracDataType`). Ces énumérations sont cruciales pour interpréter correctement les données brutes des fichiers PTRAC et pour écrire du code lisible et robuste.

**Interaction avec DECIMA :**

Dans DECIMA, `mcnptools` est principalement utilisée par le module EVA pour exécuter le code Python généré par OTACON. OTACON, quant à lui, est informé de la structure et des capacités de `mcnptools` via le 
contexte large structuré et le contexte EMMA, ce qui lui permet de générer du code Python valide et efficace qui interagit correctement avec la bibliothèque. Le `sandbox.py` s'assure que les instanciations de `Ptrac` sont correctes en détectant le mode du fichier PTRAC (binaire ou ASCII) et en patchant le code si nécessaire. Cette intégration étroite permet à DECIMA de traduire des requêtes complexes en des opérations précises sur les données PTRAC.

## 5. Déploiement et Exécution

Le projet DECIMA est une application Flask qui peut être déployée dans un environnement Python standard. Voici les étapes générales pour le déploiement et l'exécution :

### 5.1. Prérequis

*   **Python 3.8+ :** Le projet est développé en Python et nécessite une version compatible.
*   **Neo4j :** Une instance de base de données Neo4j est nécessaire pour le Knowledge Graph. Elle peut être installée localement ou accessible via un service cloud.
*   **Clé API OpenAI :** Une clé API valide pour accéder aux modèles de langage d'OpenAI (ou un service compatible) est requise pour le module OTACON.

### 5.2. Installation des Dépendances

Toutes les dépendances Python sont listées dans le fichier `requirements.txt`. Elles peuvent être installées en utilisant `pip` :

```bash
pip install -r requirements.txt
```

Il est recommandé d'utiliser un environnement virtuel (`venv` ou `conda`) pour isoler les dépendances du projet.

### 5.3. Configuration de l'Environnement

Les variables d'environnement suivantes doivent être configurées :

*   `OPENAI_API_KEY` : Votre clé API OpenAI.
*   `NEO4J_URI` : L'URI de votre instance Neo4j (ex: `bolt://localhost:7687`).
*   `NEO4J_USER` : Le nom d'utilisateur pour la connexion à Neo4j (ex: `neo4j`).
*   `NEO4J_PASSWORD` : Le mot de passe pour la connexion à Neo4j (ex: `decima123`).

Ces variables peuvent être définies directement dans l'environnement du système ou dans un fichier `.env` à la racine du projet, qui sera chargé par la bibliothèque `python-dotenv`.

### 5.4. Chargement du Knowledge Graph

Avant de lancer l'application, le Knowledge Graph doit être chargé dans Neo4j. Cela se fait en exécutant le script `neo4j_loader.py` :

```bash
python kg/loader/neo4j_loader.py
```

Ce script nettoiera la base de données Neo4j existante et la remplira avec les triplets définis dans le dossier `kg/triplets`.

### 5.5. Lancement de l'Application Flask

L'application Flask peut être lancée en exécutant le fichier `app.py` :

```bash
python app.py
```

Par défaut, l'application sera accessible à l'adresse `http://127.0.0.1:5050`. Le mode `debug=True` est activé pour le développement, ce qui permet le rechargement automatique du serveur en cas de modification du code et fournit des informations de débogage détaillées.

### 5.6. Structure des Répertoires

Le projet suit une structure de répertoires bien définie pour organiser les différents composants :

```
.
├── app.py                     # Point d'entrée principal de l'application Flask
├── data/                      # Fichiers C++ et exemples MCNP (ptrac_samples, mctal_samples)
├── doc/                       # Documentation (ce fichier)
├── frontend/                  # Interface utilisateur web (HTML, CSS, JS)
│   ├── index.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── pics/                  # Images pour le frontend
├── kg/                        # Backend du Knowledge Graph (Neo4j)
│   ├── loader/
│   │   └── neo4j_loader.py    # Script de chargement du KG
│   └── triplets/              # Fichiers JSON des triplets du KG
├── modules/                   # Modules fonctionnels (agents)
│   ├── campbell.py            # Orchestrateur principal
│   ├── emma.py                # Agent d'extraction contextuelle (KG)
│   ├── eva.py                 # Agent d'exécution de code
│   ├── otacon.py              # Agent de génération de réponse/code (LLM)
│   └── quiet.py               # Agent d'analyse de requête
├── tests/                     # Tests unitaires et d'intégration
├── tools/                     # Outils internes (sandbox)
│   └── sandbox.py             # Exécution sécurisée du code
├── uploads/                   # Dossier pour les fichiers PTRAC téléversés
└── utils/                     # Fichiers de support (NLP, contexte LLM)
    ├── keywords_fr_en.py      # Lexique bilingue et stopwords
    ├── keywords_quiet.py      # Mots-clés pour QUIET
    └── llm_basic_context/     # Contexte statique pour OTACON
        ├── kg_context_code_structure.py
        ├── kg_context_example_code.py
        └── kg_context_rules.py
```

Cette structure facilite la navigation dans le projet et la compréhension de l'organisation des différents modules.

## 6. Conclusion

Le projet DECIMA représente une avancée significative dans l'automatisation de l'analyse des données de simulation nucléaire. En combinant des techniques de traitement du langage naturel, des bases de données de graphes et des modèles de langage avancés, il offre une solution puissante et intuitive pour interroger et analyser les fichiers PTRAC. Son architecture modulaire et son approche basée sur des agents garantissent une grande flexibilité et une capacité d'évolution future. DECIMA ouvre la voie à une interaction plus naturelle et efficace avec des données scientifiques complexes, réduisant la barrière technique pour les utilisateurs et accélérant le processus de recherche et d'ingénierie.



