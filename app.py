from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from modules.campbell import CampbellOrchestrator
import os
from tools import sandbox

app = Flask(
    __name__,
    template_folder="frontend",        # pour index.html
    static_folder="frontend/static"    # pour main.js, style.css
)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PTRAC_PATH"] = None

campbell = CampbellOrchestrator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze_query", methods=["POST"])
def analyze():
    data = request.get_json()
    query = data.get("query", "")
    use_context = data.get("use_context", True)
    model_choice = data.get("model") or data.get("model_choice")
    ptrac_path = app.config.get("PTRAC_PATH", None)

    # Si le frontend envoie un modèle, on le force dans OTACON
    if model_choice:
        if hasattr(campbell.otacon_agent, "set_model_and_provider"):
            campbell.otacon_agent.set_model_and_provider(model_choice)
            print(f"[APP] ✅ Modèle forcé depuis frontend : {model_choice}")
            print(f"[APP] Provider actif : {campbell.otacon_agent.provider} | "
                  f"Model actif : {campbell.otacon_agent.model}")
        else:
            campbell.otacon_agent.model = model_choice
            print(f"[APP] ⚠️ set_model_and_provider indisponible, modèle forcé : {model_choice}")

    result = campbell.process_query(query, ptrac_path, use_context=use_context)
    return jsonify({
    "response": result.get("response", "No response."),
    "code": result.get("code", ""),
    "explanation": result.get("response", ""),   # utile pour cohérence avec OTACON
    "execution_result": result.get("execution_result", {}),
    "error": result.get("error", "")             # ✅ Ajout clé
})

@app.route("/execute_code", methods=["POST"])
def execute():
    data = request.get_json()
    code = data.get("code", "")
    allow_plots = data.get("allow_plots", False)  # <--- ajoute cette ligne
    ptrac_path = app.config.get("PTRAC_PATH", None)
    if not ptrac_path:
        return jsonify({"stderr": "Aucun fichier PTRAC chargé", "stdout": "", "output_files": []})
    from modules.eva import EVA
    eva = EVA()
    eva.load_file(ptrac_path)
    result = eva.execute_code(code, allow_plots=allow_plots) 
    return jsonify(result)

@app.route("/data/ptrac_samples", methods=["POST"])
def upload_ptrac():
    if "file" not in request.files:
        return jsonify({"status": "error", "message": "Aucun fichier fourni."})
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"status": "error", "message": "Nom de fichier vide."})
    if file:
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)
        app.config["PTRAC_PATH"] = path
        return jsonify({"status": "success", "path": path, "filename": file.filename})
    return jsonify({"status": "error", "message": "Erreur de sauvegarde."})

@app.route("/abort_execution", methods=["POST"])
def abort_execution():
    if sandbox.ACTIVE_PROCESS:
        sandbox.ACTIVE_PROCESS.terminate()
        sandbox.ACTIVE_PROCESS = None
        return jsonify({"status": "terminated"})
    return jsonify({"status": "no_active_process"})

if __name__ == "__main__":
    app.run(debug=True, port=5050)
