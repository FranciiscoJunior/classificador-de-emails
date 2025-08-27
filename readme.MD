## Classificador de Emails com Flask e NLP

Este projeto é uma aplicação web que permite analisar o conteúdo de emails, classificando-os como Produtivo ou Improdutivo, e gerando respostas automáticas adequadas a cada categoria. A aplicação usa técnicas de Processamento de Linguagem Natural (NLP) e uma API de AI para realizar a classificação e a geração de respostas.

## Tecnologias Utilizadas

## Frontend: 

HTML, CSS, JavaScript (Vanilla)

## Backend:

Python (Flask), NLP com SpaCy e NLTK

Classificação com Hugging Face Transformers (facebook/bart-large-mnli)

## API:

Hugging Face para classificação de texto

Dependências: Flask, NLTK, SpaCy

Transformers (Hugging Face)

Requests (para requisições HTTP)

Funcionalidades

## Upload de Arquivo ou Entrada de Texto:

O usuário pode enviar o conteúdo do email através de um arquivo .txt ou diretamente como texto em um campo de texto.

## Processamento do Texto:

O texto do email é pré-processado usando técnicas de NLP, como remoção de stopwords e tokenização.

## Classificação:

O conteúdo do email é classificado automaticamente como Produtivo ou Improdutivo usando um modelo de zero-shot classification da Hugging Face.

## Geração de Resposta Automática:

Com base na classificação, o sistema sugere uma resposta automática (produtiva ou improdutiva).

## Integração Web:

A interface web interage com o backend Flask via requisições AJAX para processar os emails e retornar os resultados dinamicamente.

Como Rodar o Projeto
Pré-requisitos

Python 3.x: Certifique-se de ter o Python 3.x instalado no seu sistema.

Bibliotecas: As bibliotecas necessárias estão listadas abaixo.

1. Clonando o Repositório

Clone este repositório para sua máquina local:

git clone https://github.com/seu-usuario/classificador-de-emails.git
cd classificador-de-emails

2. Instalando as Dependências

## Instale as dependências Python necessárias:

pip install -r requirements.txt


## No caso de você não ter um requirements.txt, as bibliotecas necessárias são:

pip install Flask transformers nltk spacy requests

3. Configurando o NLP (SpaCy e NLTK)

Se você estiver usando SpaCy para processamento de linguagem, será necessário baixar o modelo de idioma português:

python -m spacy download pt_core_news_sm

## Além disso, baixe os recursos do NLTK:

import nltk
nltk.download('stopwords')
nltk.download('punkt')

4. Rodando o Backend

## Navegue até o diretório onde está o arquivo app.py e execute o servidor Flask:

python app.py


O servidor Flask será iniciado em http://127.0.0.1:5000.

5. Rodando o Frontend

Abra o arquivo index.html no seu navegador. A interface web permitirá que você envie emails para análise.

O frontend se comunicará com o backend Flask, enviando o conteúdo dos emails e exibindo os resultados de classificação e resposta.

## Estrutura do Projeto

/classificador-de-emails
  ├── /static                # Arquivos estáticos (CSS, JS, Imagens)
  │   ├── /css               # Arquivos CSS
  │   └── /js                # Arquivos JavaScript
  ├── /templates             # Arquivos HTML (se usar Flask para renderizar templates)
  ├── /venv                  # Ambiente virtual Python (opcional, para dependências)
  ├── app.py                 # Backend (Flask) com a lógica de processamento de emails
  ├── config_nltk.py         # Arquivo de configuração do NLTK (baixa stopwords e tokenizer)
  ├── index.html             # Interface HTML do Frontend
  ├── styles.css             # Estilos CSS
  ├── script.js              # Lógica JavaScript para interações no Frontend
  ├── requirements.txt       # Arquivo com dependências do projeto (opcional)
  ├── .gitignore             # Arquivo para ignorar arquivos desnecessários no git (ex: ambiente virtual, arquivos temporários)
  └── README.md              # Documentação do projeto (README)

## Como Funciona:
1. Frontend (HTML + JavaScript)

O frontend oferece um formulário onde o usuário pode enviar um arquivo de texto (.txt ou .pdf) ou colar o conteúdo do email diretamente em um campo de texto.

Quando o usuário clica no botão de "Analisar Email", o conteúdo é enviado para o backend através de uma requisição AJAX (usando fetch() no JavaScript).

O resultado da classificação e da resposta gerada pelo backend é então exibido na interface.

2. Backend (Python com Flask)

O servidor Flask recebe o conteúdo do email através de uma requisição POST no endpoint /processar_email.

O texto do email é pré-processado com NLTK (remoção de stopwords, tokenização) e classificado usando um modelo de zero-shot classification da Hugging Face.

Após a classificação, o backend retorna a categoria (Produtivo ou Improdutivo) e uma resposta automática sugerida.

3. Classificação e Resposta

Classificação: O modelo de NLP classifica o texto do email em duas categorias: Produtivo ou Improdutivo.

Resposta Automática: Dependendo da categoria, o backend gera uma resposta adequada:

Produtivo: "Obrigado pelo email. Confirmamos o recebimento e seguiremos com os próximos passos."

Improdutivo: "Agradecemos o contato. No momento, este assunto não requer ação imediata."

## Melhorias Futuras

Suporte completo para PDF: Implementar a extração de texto de arquivos PDF.

Treinamento Personalizado: Treinar um modelo de classificação específico para o domínio do usuário.

Melhoria de UI/UX: Tornar a interface mais interativa e visualmente agradável, talvez com gráficos ou feedbacks mais dinâmicos.

## Armazenamento e Histórico: Implementar a capacidade de armazenar e consultar emails analisados anteriormente.

Contribuições

## Se você quiser contribuir para este projeto, basta seguir os passos abaixo:

Faça um fork do repositório. Crie uma nova branch para a sua funcionalidade: git checkout -b minha-nova-funcionalidade. Faça as alterações e comite-as: git commit -am 'Adiciona nova funcionalidade'. Envie para o repositório remoto: git push origin minha-nova-funcionalidade.

Abra um Pull Request explicando suas alterações.

Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.