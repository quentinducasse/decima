@echo off
setlocal

echo [VENOM] 🧪 Initialisation du build MCNPTools pour environnement virtuel...

REM === Chemins à adapter si besoin ===
set MCNPTOOLS_SRC=C:\Users\qduca\OneDrive\Softwares\mcnptools-main\mcnptools-main
set MCNPTOOLS_BUILD=%MCNPTOOLS_SRC%\build
set MCNPTOOLS_INSTALL=C:\Users\qduca\OneDrive\Applications\DECIMA_v2\decima_env\mcnptools_install
set HDF5_ROOT=C:\HDF_Group\HDF5\1.14.6
set VENV_PYTHON=C:\Users\qduca\OneDrive\Applications\DECIMA_v2\decima_env\Scripts\python.exe

REM === Nettoyage partiel du build pour éviter les conflits CMake ===
echo [VENOM] ♻️ Nettoyage du cache de CMake...
del /Q "%MCNPTOOLS_BUILD%\CMakeCache.txt" >nul 2>&1
rmdir /S /Q "%MCNPTOOLS_BUILD%\CMakeFiles" >nul 2>&1

REM === Étape 1 : Configuration CMake ===
echo [VENOM] ⚙️ Configuration CMake...
cmake -S "%MCNPTOOLS_SRC%" -B "%MCNPTOOLS_BUILD%" ^
 -DCMAKE_INSTALL_PREFIX="%MCNPTOOLS_INSTALL%" ^
 -DHDF5_ROOT="%HDF5_ROOT%" ^
 -DCMAKE_GENERATOR_PLATFORM=x64 ^
 -DCMAKE_BUILD_TYPE=Release

if errorlevel 1 (
    echo [ERREUR] ❌ Échec configuration CMake
    exit /b 1
)

REM === Étape 2 : Build ===
echo [VENOM] 🔧 Compilation...
cmake --build "%MCNPTOOLS_BUILD%" --config Release --target install

if errorlevel 1 (
    echo [ERREUR] ❌ Échec compilation
    exit /b 1
)

REM === Étape 3 : Installation Python dans l'environnement virtuel ===
echo [VENOM] 🐍 Installation dans l'environnement virtuel Python...
cd /D "%MCNPTOOLS_BUILD%\python"
"%VENV_PYTHON%" setup.py install

if errorlevel 1 (
    echo [ERREUR] ❌ Échec installation Python
    exit /b 1
)

echo [VENOM] ✅ MCNPTools installé dans l’environnement virtuel avec succès !
endlocal
