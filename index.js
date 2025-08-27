    document.getElementById('emailForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const textArea = document.getElementById('emailText');
    const categoria = document.getElementById('categoria');
    const resposta = document.getElementById('resposta');
    const resultSection = document.getElementById('resultSection');

    let emailContent = "";

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const allowedTypes = ['text/plain', 'application/pdf'];

        if (!allowedTypes.includes(file.type)) {
        alert('Formato de arquivo não suportado. Envie .txt ou .pdf');
        return;
        }

        const reader = new FileReader();
        reader.onload = async function(e) {
        emailContent = e.target.result;
        await processEmail(emailContent);
        };
        reader.readAsText(file);

    } else if (textArea.value.trim() !== "") {
        emailContent = textArea.value.trim();
        await processEmail(emailContent);
    } else {
        alert("Insira um texto ou envie um arquivo para análise.");
    }

    async function processEmail(texto) {
        try {
        // Enviar requisição POST para o backend
        const response = await fetch("http://127.0.0.1:5000/processar_email", {
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify({ emailText: texto })
        });

        const result = await response.json();

        // Exibir os resultados
        categoria.textContent = result.category;
        resposta.textContent = result.response;
        resultSection.style.display = "block";

        } catch (error) {
        console.error("Erro ao processar email:", error);
        }
    }
    });
