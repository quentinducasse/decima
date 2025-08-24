document.addEventListener("DOMContentLoaded", function () {
  const sendBtn = document.getElementById("send-btn");
  const inputField = document.getElementById("query-input");
  const chatMessages = document.getElementById("chat-messages");
  const stdoutBlock = document.getElementById("execution-stdout");
  const stderrBlock = document.getElementById("execution-stderr");
  const imageBlock = document.getElementById("execution-image");
  const resultSection = document.getElementById("result-section");
  const ptracFileInput = document.getElementById("ptrac-file");
  const fileInfo = document.getElementById("file-info");

  let latestLLMCode = ""; 

  document.getElementById("open-file-btn").addEventListener("click", () => {
    ptracFileInput.click();
  });

  ptracFileInput.addEventListener("change", function () {
    const file = this.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    fetch("/data/ptrac_samples", {
      method: "POST",
      body: formData
    })
      .then((r) => r.json())
      .then((data) => {
        if (data.status === "success") {
          fileInfo.textContent = `Fichier chargé : ${data.filename}`;
        } else {
          fileInfo.textContent = `Erreur : ${data.message}`;
        }
      });
  });

  function addMessage(content, role = "user") {
    const div = document.createElement("div");
    div.className = `message ${role}-message`;
    div.innerHTML = `<div class="message-content">${content}</div>`;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function addAssistantMessage(response, code) {
    const div = document.createElement("div");
    div.className = "message assistant-message";
    let codeHtml = "";
    if (code) {
      latestLLMCode = code; 
      codeHtml = `
        <div class="code-block">
          <div class="code-header">
            <span>Python</span>
            <button class="copy-btn"><i class="fas fa-copy"></i></button>
          </div>
          <pre><code id="llm-code-block" class="language-python">${hljs.highlight(code, { language: 'python' }).value}</code></pre>
          <button class="execute-btn">Exécuter le code</button>
        </div>`;
    }
    div.innerHTML = `<div class="message-content">${response}</div>${codeHtml}`;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    const copyBtn = div.querySelector(".copy-btn");
    if (copyBtn) {
      copyBtn.onclick = () => {
        navigator.clipboard.writeText(code);
      };
    }

    const execBtn = div.querySelector(".execute-btn");
    if (execBtn) {
  const stopBtn = document.createElement("button");
  stopBtn.className = "stop-btn inline";
  stopBtn.textContent = "Stop Code Generation";
  stopBtn.style.display = "none"; 

  execBtn.parentNode.insertBefore(stopBtn, execBtn.nextSibling);

  execBtn.onclick = () => {
    stopBtn.style.display = "inline-block";

    fetch("/execute_code", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code: latestLLMCode, allow_plots: true })
    })
      .then(r => r.json())
      .then(data => {
        resultSection.style.display = "block";
        stdoutBlock.textContent = data.stdout || "";
        stderrBlock.textContent = data.stderr || "";
        if (data.output_files && data.output_files.length > 0) {
          imageBlock.src = `/download_file?path=${encodeURIComponent(data.output_files[0])}`;
          imageBlock.style.display = "block";
        } else {
          imageBlock.style.display = "none";
        }
        stopBtn.style.display = "none"; 
      });
  };

  stopBtn.onclick = () => {
    stopBtn.style.display = "none";
    fetch("/abort_execution", { method: "POST" })
      .then(r => r.json())
      .then(data => {
        console.warn("⛔️ Code interrompu :", data.status);
        stderrBlock.textContent += `\n⛔️ Manual interruption: ${data.status}`;
      })
      .catch(() => {
        stderrBlock.textContent += `\n⛔️ Error: unable to interrupt the process`;
      });
  };

}

  }

  sendBtn.onclick = () => {
  const query = inputField.value;
  if (!query) return;

  const useContext = document.getElementById("context-toggle").checked;

  const modelSelect = document.getElementById("model-choice");
  const modelChoice = modelSelect ? modelSelect.value : null;

  const reasoningLoader = document.getElementById("reasoning-loader");
  reasoningLoader.style.display = "flex";

  addMessage(query, "user");
  inputField.value = "";

  fetch("/analyze_query", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ 
    query, 
    use_context: useContext, 
    model: modelChoice            
  })
})
  .then((r) => r.json())
  .then((data) => {
    reasoningLoader.style.display = "none";

    if (data.explanation && data.explanation.includes("[ERROR:INVALID_API_KEY]")) {
      addAssistantMessage(`
        <div style="color:#ff4444; font-weight:bold;">
          ❌ Invalid API key.<br>
          Please edit your <code>.env</code> file and set a valid <code>OPENAI_API_KEY</code>.<br>
          Restart DECIMA after saving the file.
        </div>
      `, null);
      return; 
    }
    if ((data.error && data.error.toLowerCase().includes("no entities detected")) ||
        (data.explanation && data.explanation.toLowerCase().includes("pas d'entités emma"))) {
      addAssistantMessage(`
        <div style="color:#ff4444; font-weight:bold;">
          ⚠️ No entities were detected.<br>
          Make sure Neo4j Desktop is running and the <code>DECIMA graph</code> database is started.<br>
          Then retry your query.
        </div>
      `, null);
}

    addAssistantMessage(data.response, data.code);
    resultSection.style.display = "none";
    stdoutBlock.textContent = "";
    stderrBlock.textContent = "";
    imageBlock.style.display = "none";
  });
};

  const stopCodeBtn = document.getElementById("stop-code-btn");

  document.addEventListener("click", function (event) {
    if (event.target && event.target.classList.contains("execute-btn")) {
      stopCodeBtn.style.display = "inline-block";
    }
  });

  stopCodeBtn.addEventListener("click", () => {
    console.warn("⛔️ Code interrupted by user");
    stopCodeBtn.style.display = "none";
    stderrBlock.textContent += "\n⛔️ Manual (simulated) interruption";
  });

document.getElementById("send-btn").addEventListener("click", () => {
  const query = document.getElementById("query-input").value;
  const addContext = document.getElementById("context-toggle").checked;
  const modelChoice = document.getElementById("model-choice").value;

  fetch("/process_query", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      query: query,
      use_context: addContext,
      model: modelChoice
    })
  })
  .then(res => res.json())
  .then(data => {
    // affichage du résultat (inchangé)
  });
});
  
});
