from flask import Flask, request, jsonify
import spacy
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Inicializando o Flask
app = Flask(__name__)

# Carregar o modelo de NLP (spaCy) para remoção de stopwords
nlp = spacy.load("pt_core_news_sm")
nltk.download('stopwords')

# Inicializando a API de IA para classificação (Transformers HuggingFace)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Função para limpar o texto (NLP)
def clean_text(text):
    # Tokenizar e remover stopwords usando NLTK
    stop_words = set(stopwords.words("portuguese"))
    word_tokens = word_tokenize(text.lower())
    cleaned_text = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return " ".join(cleaned_text)

# Função para classificar o email
def classify_email(text):
    # Candidatos para a classificação
    candidate_labels = ["Produtivo", "Improdutivo"]

    # Classificação utilizando o modelo de NLP Hugging Face
    result = classifier(text, candidate_labels)
    category = result["labels"][0]
    return category

# Função para gerar uma resposta automática
def generate_response(category):
    if category == "Produtivo":
        return "Obrigado pelo email. Confirmamos o recebimento e seguiremos com os próximos passos."
    else:
        return "Agradecemos o contato. No momento, este assunto não requer ação imediata."

@app.route("/processar_email", methods=["POST"])
def process_email():
    # Obter dados do frontend (HTML)
    data = request.json
    email_text = data.get("emailText", "")

    # Limpeza do texto
    cleaned_text = clean_text(email_text)

    # Classificar o email
    category = classify_email(cleaned_text)

    # Gerar resposta
    response = generate_response(category)

    return jsonify({"category": category, "response": response})

if __name__ == "__main__":
    app.run(debug=True)