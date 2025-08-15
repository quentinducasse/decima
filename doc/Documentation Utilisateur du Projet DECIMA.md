# Documentation Utilisateur du Projet DECIMA

**Auteur :** Manus AI

**Date :** 1er août 2025

## 1. Introduction à DECIMA

Bienvenue dans DECIMA (Data Extraction & Contextual Inference for MCNP Analysis) ! DECIMA est un outil intelligent conçu pour vous aider à analyser et à comprendre facilement les fichiers de trajectoires de particules (PTRAC) générés par le code de simulation nucléaire MCNP. Que vous soyez ingénieur, chercheur ou étudiant, DECIMA simplifie l'accès aux informations complexes contenues dans vos simulations.

Traditionnellement, l'analyse des fichiers PTRAC nécessite une connaissance approfondie de la programmation et de la structure interne de ces fichiers. DECIMA change la donne en vous permettant de poser des questions en langage naturel (comme vous le feriez à un collègue) et d'obtenir des réponses précises, souvent accompagnées de code Python que vous pouvez exécuter pour valider ou approfondir l'analyse.

**Avec DECIMA, vous pouvez :**

*   **Poser des questions intuitives :** Décrivez ce que vous voulez savoir sur votre fichier PTRAC en français ou en anglais.
*   **Obtenir des explications claires :** DECIMA vous fournit des réponses détaillées et compréhensibles.
*   **Générer du code Python :** Pour les analyses complexes, DECIMA génère automatiquement le code Python nécessaire, prêt à être exécuté.
*   **Visualiser les résultats :** Exécutez le code généré pour voir les données brutes ou même des graphiques (si le code le permet).

Ce guide utilisateur vous accompagnera pas à pas pour tirer le meilleur parti de DECIMA, de la préparation de votre environnement à l'interprétation des résultats.




## 2. Démarrage Rapide

Pour commencer à utiliser DECIMA, suivez ces étapes simples :

### 2.1. Accéder à l'Application

DECIMA est une application web. Une fois que l'administrateur du système a lancé l'application, vous pouvez y accéder via votre navigateur web à l'adresse suivante (par défaut) :

`http://127.0.0.1:5050`

Vous devriez voir l'interface principale de DECIMA, prête à recevoir vos requêtes.

### 2.2. Charger un Fichier PTRAC

Avant de poser des questions, vous devez charger le fichier PTRAC que vous souhaitez analyser. C'est une étape cruciale car DECIMA effectuera toutes ses analyses sur ce fichier.

1.  **Cliquez sur le bouton "Load PTRAC File"** (ou "Charger Fichier PTRAC" si l'interface est localisée en français). Ce bouton est généralement situé en haut de la page.
2.  Une fenêtre de sélection de fichier s'ouvrira. **Naviguez jusqu'à l'emplacement de votre fichier PTRAC** sur votre ordinateur et sélectionnez-le.
3.  Une fois le fichier sélectionné, son nom devrait apparaître à côté du bouton, confirmant qu'il a été chargé avec succès dans l'application. Si un message d'erreur apparaît, vérifiez le format de votre fichier ou réessayez.

**Important :** DECIMA ne peut analyser qu'un seul fichier PTRAC à la fois. Si vous chargez un nouveau fichier, il remplacera le précédent.

### 2.3. Poser une Question

Maintenant que votre fichier PTRAC est chargé, vous pouvez interroger DECIMA.

1.  **Saisissez votre question** dans la zone de texte située en bas de l'interface de chat. Soyez aussi précis et concis que possible. DECIMA est conçu pour comprendre le langage naturel, mais une question bien formulée donnera de meilleurs résultats.
    *   **Exemples de questions :**
        *   "Affiche la position x, y, z et l'énergie des neutrons qui traversent la surface 12."
        *   "Combien de photons secondaires sont émis par diffusion inélastique ?"
        *   "Quelle est la distribution d'énergie des neutrons de fission (n,xn) générés ?"
2.  **Cochez ou décochez la case "Add context"** (Ajouter contexte) :
    *   **Coché (par défaut) :** DECIMA utilisera son Knowledge Graph pour enrichir sa compréhension de votre question. C'est recommandé pour la plupart des requêtes, car cela aide DECIMA à être plus précis.
    *   **Décoché :** DECIMA répondra sans utiliser le contexte de son Knowledge Graph. Cela peut être utile pour des questions très génériques ou si vous rencontrez des problèmes avec l'ajout de contexte.
3.  **Cliquez sur le bouton "Envoyer"** (l'icône d'avion en papier) à droite de la zone de texte.

DECIMA va alors traiter votre requête. Un message "Reasoning..." (Réflexion en cours...) apparaîtra pendant que le système analyse votre question et génère une réponse.

### 2.4. Interpréter la Réponse de DECIMA

Une fois le traitement terminé, DECIMA affichera sa réponse dans la zone de chat. La réponse se compose généralement de deux parties :

1.  **Explication en langage naturel :** Une description claire et pédagogique de la réponse à votre question, expliquant les concepts et les résultats.
2.  **Bloc de code Python :** Pour les questions nécessitant une analyse de données, DECIMA générera un script Python utilisant la bibliothèque `mcnptools`. Ce code est la traduction de votre question en instructions de programmation.

### 2.5. Exécuter le Code Python

Le code Python généré par DECIMA n'est pas exécuté automatiquement. Vous avez la possibilité de le faire manuellement pour voir les résultats concrets.

1.  **Cliquez sur le bouton "Exécuter le code"** situé sous le bloc de code Python.
2.  DECIMA exécutera le code dans un environnement sécurisé (sandbox) en utilisant le fichier PTRAC que vous avez chargé.
3.  Les résultats de l'exécution apparaîtront dans la section "Execution Result" (Résultat d'exécution) en bas de la page :
    *   **Stdout :** La sortie standard du script (par exemple, les valeurs numériques, les messages `print`).
    *   **Stderr :** Les messages d'erreur ou d'avertissement générés pendant l'exécution du code.
    *   **Image :** Si le code génère un graphique (par exemple, une distribution d'énergie), l'image sera affichée ici.

**Interrompre l'exécution :** Si un script prend trop de temps ou semble bloqué, un bouton "Stop Code Generation" (Arrêter la génération de code) apparaîtra. Cliquez dessus pour arrêter l'exécution.




## 3. Utilisation Avancée

### 3.1. Formulation des Questions Efficaces

Pour obtenir les meilleurs résultats de DECIMA, il est utile de comprendre comment formuler vos questions. Pensez à la manière dont vous décririez votre problème à un expert humain qui connaîtrait `mcnptools` et les fichiers PTRAC.

*   **Soyez précis :** Au lieu de "Donne-moi des infos sur les neutrons", demandez "Quelle est l'énergie moyenne des neutrons qui traversent la surface 300 ?"
*   **Utilisez le vocabulaire MCNP/PTRAC :** Mentionnez les termes comme "événement", "histoire", "particule", "cellule", "surface", "énergie", "poids", "temps", "ZAID", "réaction", "banque", etc.
*   **Spécifiez les conditions :** Si vous cherchez des données pour une particule, une cellule ou une surface spécifique, incluez son identifiant (ex: "neutrons", "cellule 200", "surface 300").
*   **Indiquez le type de résultat souhaité :** "Affiche", "Calcule", "Trace", "Donne le nombre de", "Quelle est la moyenne de", "Liste les...", etc.
*   **Questions complexes :** DECIMA peut gérer des questions multi-critères. Par exemple : "Affiche la position x, y, z et l'énergie des 5 premiers électrons de la première histoire qui ont une énergie supérieure à 1 MeV et qui sont générés par un événement de banque de type photo-électron."

### 3.2. Comprendre le Contexte du LLM

La case à cocher "Add context" contrôle si DECIMA utilise son Knowledge Graph (KG) pour enrichir la compréhension de votre question. Voici quand et pourquoi vous pourriez vouloir la modifier :

*   **Contexte activé (par défaut et recommandé) :** Lorsque cette option est cochée, DECIMA interroge son KG pour trouver des informations pertinentes sur les classes `mcnptools`, les énumérations, les dictionnaires (comme les types de réactions MT ou les codes de particules) et leurs relations. Cela aide le LLM (OTACON) à générer un code plus précis et à éviter les erreurs, car il dispose d'une connaissance structurée des outils et des données PTRAC.
    *   **Avantage :** Réponses plus pertinentes et code plus fiable pour les questions complexes ou spécifiques.
    *   **Inconvénient :** Peut parfois introduire des entités non pertinentes si votre question est ambiguë, ou ralentir légèrement le traitement.

*   **Contexte désactivé :** Si vous décochez cette option, DECIMA s'appuiera uniquement sur les connaissances générales de son modèle de langage et sur les exemples de code qu'il a appris. Il n'interrogera pas le KG.
    *   **Avantage :** Peut être plus rapide pour des questions très simples ou si vous avez l'impression que le contexte du KG "perturbe" la réponse du LLM pour une raison quelconque.
    *   **Inconvénient :** Le LLM peut être moins précis ou générer du code incorrect s'il manque des informations spécifiques sur `mcnptools` ou les conventions PTRAC.

En général, il est conseillé de laisser le contexte activé, sauf si vous rencontrez des problèmes spécifiques ou si vous souhaitez expérimenter.

### 3.3. Analyse des Résultats d'Exécution

Après avoir exécuté le code généré, la section "Execution Result" vous fournit des informations cruciales :

*   **`stdout` (Standard Output) :** C'est ici que le script Python affiche ses résultats. Si le code est conçu pour imprimer des valeurs, des listes ou des messages, ils apparaîtront ici. C'est la sortie "normale" du programme.
*   **`stderr` (Standard Error) :** Cette section affiche les messages d'erreur ou les avertissements générés par le script Python. Si votre code ne s'exécute pas comme prévu, ou si une erreur de programmation se produit, les détails de l'erreur seront ici. Lisez attentivement ces messages pour comprendre ce qui n'a pas fonctionné.
*   **Image :** Si le code Python généré inclut des instructions pour créer des graphiques (par exemple, avec `matplotlib`), l'image résultante sera affichée dans cette section. Cela vous permet de visualiser directement les distributions, les tendances ou d'autres représentations graphiques de vos données PTRAC.

**Conseils pour le débogage :**
*   Si `stderr` contient des erreurs, lisez la dernière ligne pour identifier le type d'erreur et la ligne de code concernée. Cela vous aidera à comprendre si le problème vient du code généré ou de vos données PTRAC.
*   Si `stdout` est vide alors que vous attendiez une sortie, vérifiez que le code Python contient bien des instructions `print()` pour afficher les résultats.
*   Si l'image ne s'affiche pas, assurez-vous que le code généré inclut bien des commandes de plotting et que `allow_plots` est activé lors de l'exécution (ce qui est le cas via l'interface web).




## 4. Dépannage et Questions Fréquentes

Cette section aborde les problèmes courants que vous pourriez rencontrer en utilisant DECIMA et propose des solutions.

### 4.1. Problèmes de Chargement de Fichier PTRAC

*   **"Aucun fichier fourni." ou "Nom de fichier vide."**
    *   **Cause :** Vous n'avez pas sélectionné de fichier ou le fichier sélectionné n'a pas de nom valide.
    *   **Solution :** Assurez-vous de bien choisir un fichier via la boîte de dialogue. Vérifiez que le nom du fichier ne contient pas de caractères spéciaux qui pourraient poser problème.
*   **"Erreur de sauvegarde."**
    *   **Cause :** Le système n'a pas pu enregistrer le fichier PTRAC dans le dossier temporaire `uploads`.
    *   **Solution :** Contactez l'administrateur du système. Il pourrait s'agir d'un problème de permissions ou d'espace disque.
*   **Le fichier est chargé, mais les analyses ne fonctionnent pas.**
    *   **Cause :** Le fichier PTRAC est corrompu ou n'est pas dans un format reconnu par `mcnptools`.
    *   **Solution :** Vérifiez l'intégrité de votre fichier PTRAC avec MCNP ou un autre outil. Assurez-vous qu'il s'agit bien d'un fichier PTRAC valide (binaire ou ASCII).

### 4.2. Problèmes de Réponse du LLM (OTACON)

*   **La réponse est générique ou ne contient pas de code.**
    *   **Cause :** La question est trop vague, ou le LLM n'a pas compris l'intention de générer du code.
    *   **Solution :** Reformulez votre question pour être plus précis. Utilisez des verbes d'action comme "Affiche", "Calcule", "Génère le code pour", "Trace la distribution de". Assurez-vous que votre question est directement liée à l'analyse de données PTRAC.
*   **Le code généré est incorrect ou ne correspond pas à la question.**
    *   **Cause :** Le LLM a mal interprété votre requête, ou le contexte fourni par EMMA était insuffisant/erroné.
    *   **Solution :**
        *   **Vérifiez la case "Add context" :** Si elle est décochée, essayez de la cocher. Si elle est déjà cochée, essayez de la décocher pour voir si cela améliore la situation (rare, mais possible).
        *   **Reformulez la question :** Essayez d'utiliser des synonymes ou de simplifier la question. Évitez les ambiguïtés.
        *   **Vérifiez les termes techniques :** Assurez-vous que les termes MCNP/PTRAC que vous utilisez sont corrects et courants.
*   **"Reasoning..." reste affiché longtemps.**
    *   **Cause :** Le LLM prend du temps à générer la réponse, ou il y a un problème de connexion avec l'API OpenAI.
    *   **Solution :** Patientez quelques instants. Si le problème persiste, vérifiez votre connexion internet. Si vous êtes l'administrateur, vérifiez les logs du serveur Flask et la configuration de la clé API OpenAI.

### 4.3. Problèmes d'Exécution de Code (EVA)

*   **"Aucun fichier PTRAC chargé." (dans `stderr` après exécution).**
    *   **Cause :** Vous avez tenté d'exécuter du code sans avoir préalablement chargé un fichier PTRAC.
    *   **Solution :** Chargez un fichier PTRAC en suivant les étapes de la section 2.2.
*   **"Timeout: exécution trop longue." (dans `stderr`).**
    *   **Cause :** Le code généré est entré dans une boucle infinie, est trop complexe, ou le fichier PTRAC est très grand et l'analyse prend trop de temps.
    *   **Solution :**
        *   **Interrompez l'exécution :** Utilisez le bouton "Stop Code Generation" si disponible.
        *   **Simplifiez la requête :** Demandez une analyse sur un sous-ensemble de données (ex: "les 10 premières histoires" au lieu de "toutes les histoires").
        *   **Vérifiez le code :** Si vous avez des connaissances en Python, examinez le code généré pour identifier d'éventuelles boucles ou opérations coûteuses.
*   **Erreurs Python dans `stderr` (ex: `NameError`, `AttributeError`, `IndexError`).**
    *   **Cause :** Le code généré contient des erreurs de syntaxe, utilise des fonctions ou attributs inexistants, ou tente d'accéder à des données qui ne sont pas présentes dans le fichier PTRAC.
    *   **Solution :**
        *   **Lisez le message d'erreur :** Il indique la ligne et le type d'erreur. Cela peut vous donner des indices sur la cause.
        *   **Reformulez la question :** Si l'erreur semble liée à une mauvaise compréhension du LLM, essayez de poser la question différemment.
        *   **Vérifiez le fichier PTRAC :** Assurez-vous que les données que vous demandez existent réellement dans votre fichier PTRAC (par exemple, si vous demandez des électrons, assurez-vous que votre simulation en a produit).
*   **L'image du plot ne s'affiche pas.**
    *   **Cause :** Le code généré ne contient pas d'instructions de plotting, ou il y a eu une erreur pendant la génération du graphique.
    *   **Solution :** Assurez-vous que votre question implique une visualisation (ex: "trace la distribution", "affiche un histogramme"). Vérifiez le `stderr` pour d'éventuelles erreurs liées au plotting.

### 4.4. Questions Générales

*   **Puis-je utiliser DECIMA avec n'importe quel fichier MCNP ?**
    *   DECIMA est spécifiquement conçu pour analyser les fichiers **PTRAC** générés par MCNP. Il ne peut pas analyser directement les fichiers d'entrée MCNP (`.inp`) ou les fichiers de sortie (`.out`) complets, sauf si ces derniers contiennent des données PTRAC.
*   **Mes données sont-elles sécurisées ?**
    *   Les fichiers PTRAC que vous téléchargez sont traités localement sur le serveur où DECIMA est déployé. Le code généré par le LLM est exécuté dans un environnement sandboxisé pour des raisons de sécurité. Cependant, la confidentialité de vos données dépend de la configuration et de la sécurité du serveur sur lequel DECIMA est hébergé. Pour des données très sensibles, consultez votre administrateur système.
*   **Puis-je modifier le code Python généré ?**
    *   Oui, vous pouvez copier le code généré et le modifier dans votre propre environnement Python si vous le souhaitez. DECIMA est un assistant, mais vous gardez le contrôle total sur l'analyse finale.



