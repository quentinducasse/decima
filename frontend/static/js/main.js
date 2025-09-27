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

  // === File upload ===
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
          fileInfo.textContent = `File loaded: ${data.filename}`;
        } else {
          fileInfo.textContent = `Error: ${data.message}`;
        }
      });
  });

  // === Chat messages ===
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
          <button class="execute-btn">Run Code</button>
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
      stopBtn.textContent = "Stop Code Execution";
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
            console.warn("⛔️ Code interrupted:", data.status);
            stderrBlock.textContent += `\n⛔️ Manual interruption: ${data.status}`;
          })
          .catch(() => {
            stderrBlock.textContent += `\n⛔️ Error: unable to interrupt the process`;
          });
      };
    }
  }

  // === Knowledge Graph Warning ===
  function showKgWarning(show = true, msg) {
    const banner = document.getElementById("kg-warning");
    if (!banner) return;
    if (msg) {
      banner.innerHTML = `<i class="fas fa-triangle-exclamation"></i> ${msg}`;
    }
    banner.style.display = show ? "flex" : "none";
  }

  // === Send query ===
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

        // === Knowledge Graph warning (simplified + clear) ===
        if (data?.emma) {
          const e = data.emma;
          if (e.requested && !e.ok && !e.skipped) {
            let technical = e.error
              ? e.error.replace(/^\[EMMA ERROR\]\s*/, "")
              : e.warning.replace(/^\[EMMA WARNING\]\s*/, "");
            const msg = `
              <strong>Knowledge Graph connection issue:</strong><br>
              <span style="font-size:0.9em; color:#ddd;">${technical}</span><br><br>
              ⚠️ The request will continue, but Otacon will not benefit from the full Knowledge Graph context and may be more prone to mistakes.<br><br>
              ➡️ To enable full context, make sure Neo4j is running and load the Knowledge Graph with:<br>
              <code>docker compose exec app python kg/loader/neo4j_loader.py</code><br>
              (see README.md for details)
            `;
            showKgWarning(true, msg);
          } else {
            showKgWarning(false);
          }
        }


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

        addAssistantMessage(data.response, data.code);
        resultSection.style.display = "none";
        stdoutBlock.textContent = "";
        stderrBlock.textContent = "";
        imageBlock.style.display = "none";
      });
  };

  // === Stop code button (global) ===
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
});
