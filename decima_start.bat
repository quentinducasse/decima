@echo off
title DECIMA Starter

:: === Vérification de Python installé ===
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [❌] Python n'est pas reconnu comme une commande interne.
    echo [💡] Veuillez installer Python 3.8+ et l'ajouter au PATH.
    pause
    exit /b
)

:: === Activation de l'environnement virtuel ===
IF NOT EXIST "decima_env\Scripts\activate.bat" (
    echo [❌] L'environnement virtuel 'decima_env' est introuvable.
    echo [💡] Créez-le avec : python -m venv decima_env
    echo      Puis installez les dépendances avec : pip install -r requirements.txt
    pause
    exit /b
)

call decima_env\Scripts\activate.bat
echo [✅] Environnement virtuel activé.

:: === Lancement de Neo4j Desktop ===
echo.
echo [STEP 1] Lancement de Neo4j Desktop (si installé à l'emplacement par défaut)...

SET "NEO4J_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Neo4j Desktop\Neo4j Desktop.exe"
IF EXIST "%NEO4J_PATH%" (
    start "" "%NEO4J_PATH%"
    echo [✅] Neo4j Desktop ouvert.
) ELSE (
    echo [⚠️] Neo4j Desktop introuvable à l'emplacement par défaut.
    echo [ℹ️] Si installé ailleurs, veuillez le lancer manuellement.
)

echo.
echo [⏳] Veuillez maintenant démarrer votre base de données Neo4j (ex: DECIMA GRAPH).
pause

:: === Chargement du Knowledge Graph ===
echo.
echo [STEP 2] Chargement du graphe de connaissances dans Neo4j...
python kg\loader\neo4j_loader.py
IF %ERRORLEVEL% NEQ 0 (
    echo [❌] Échec du chargement du graphe. Vérifiez que Neo4j est bien démarré.
    pause
    exit /b
)
echo [✅] Graphe chargé avec succès.

:: === Lancement de l'application Flask ===
echo.
echo [STEP 3] Lancement de l'application DECIMA...
python app.py

echo.
echo [✅] L'application est lancée sur http://127.0.0.1:5050
pause
