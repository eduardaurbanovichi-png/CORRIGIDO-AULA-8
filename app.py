
# #exemplo da professora


# import streamlit as st # precisa instalar 
# import spacy# precisa instalar 
# import nltk# precisa instalar 
# from nltk.sentiment import SentimentIntensityAnalyzer
# from deep_translator import GoogleTranslator
# from nltk import word_tokenize
# from nltk.corpus import stopwords



# # Garante o download do dicionário VADER
# nltk.download('vader_lexicon', quiet=True)
# nltk.download('punkt_tab', quiet=False)
# nltk.download('stopwords', quiet=True)

# nlp = spacy.load("pt_core_news_sm")

# # Configuração da interface
# st.title("Análise de Sentimentos em Português")

# # Agora o usuário pode digitar em português
# texto_pt = st.text_area("Digite seu texto em português:", "Eu adoro este produto! É maravilhoso.")

# if st.button("Analisar Sentimento"):
#     fat =   nltk.word_tokenize(texto_pt)
#     stops = set(stopwords.words('portuguese'))
#     palavras_uteis = [t for t in fat if t.isalnum() and t not in stops]
#     documento = nlp(texto_pt)
    
#     # Traduz o texto de português (pt) para inglês (en)
#     texto_en = GoogleTranslator(source='pt', target='en').translate(texto_pt)
    
#     # Inicializa o analisador e calcula os scores no texto traduzido
#     sia = SentimentIntensityAnalyzer()
#     scores = sia.polarity_scores(texto_en)
#     score_compound = scores['compound']
    
#     # Classifica o sentimento com base no score
#     if score_compound >= 0.05:
#         resultado = "Positivo"
#     elif score_compound <= -0.05:
#         resultado = "Negativo"
#     else:
#         resultado = "Neutro"
        

#     for token in documento:
#         st.success(f"{token.text} -> {token.pos_} ({spacy.explain(token.pos_)})")
   
#     st.subheader(f"Resultado: {resultado}")
#     st.write(f"**Score Compound:** {score_compound:.4f}")
#     st.caption(f"Texto traduzido para análise: *\"{texto_en}\"*")
#     st.write(f'TOKENIZAÇÃO - ,  {fat}')
#     st.warning(f'STOP WORDS -, {palavras_uteis}')





# EXERCICIO 1


# faça:

# Contexto

# Uma empresa recebe centenas de mensagens de clientes 
# todos os dias

# Objetivo

# Ela precisa separar automaticamente o texto em 
# palavras para facilitar a análise e organização das 
# informações.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Audiência

# Iniciante em NLP que quer ver o básico funcionando.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 




import streamlit as st
import nltk
from nltk.tokenize import word_tokenize



# Baixa o recurso necessário para tokenização
nltk.download('punkt', quiet=True)

# Título da aplicação
st.title("Exercício 1 - Simulador de Análise de Sentimento com Tokenização")

# Lista simples de palavras para simular sentimento
palavras_positivas = ["bom", "ótimo", "excelente", "feliz", "incrível", "bom"]
palavras_negativas = ["ruim", "péssimo", "horrível", "triste", "lento", "fraco"]

# Entrada do usuário
texto = st.text_area(
    "Digite um texto:",
    "O serviço foi ruim, mas o atendimento foi bom."
)

# Botão para analisar
if st.button("Analisar Texto", key="btn_freq"):

    # Tokenização (separar em palavras)
    tokens = word_tokenize(texto.lower())

    # Contadores simples
    positivos = 0
    negativos = 0

    # Análise palavra por palavra
    for palavra in tokens:
        if palavra in palavras_positivas:
            positivos += 1
        elif palavra in palavras_negativas:
            negativos += 1

    # Decisão final
    if positivos > negativos:
        resultado = "Sentimento Positivo 😊"
    elif negativos > positivos:
        resultado = "Sentimento Negativo 😡"
    else:
        resultado = "Sentimento Neutro 😐"

    # Resultados na tela
    st.subheader("Resultado da Análise")
    st.write(resultado)

    st.write("### Tokens encontrados:")
    st.write(tokens)

    st.write("### Contagem:")
    st.write(f"Positivos: {positivos}")
    st.write(f"Negativos: {negativos}")


# EXERCICIO 2


# faça:

# Contexto

# Um sistema de análise de dados precisa identificar quais palavras aparecem com mais frequência em 
# avaliações de clientes para entender padrões de comportamento.

# Objetivo

# Conte a frequência das palavras em um texto simples.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd

# Downloads necessários
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Título
st.title("Exercício 2 - Análise de Frequência de Palavras")

# Entrada do usuário
texto = st.text_area(
    "Digite uma avaliação:",
    "O produto é bom, muito bom e o atendimento também é excelente e bom."
)

# Botão
if st.button("Analisar Texto"):

    # ---------------------------
    # TOKENIZAÇÃO
    # ---------------------------
    tokens = word_tokenize(texto.lower())

    # Remove pontuação e números
    tokens_limpos = [t for t in tokens if t.isalpha()]

    # ---------------------------
    # STOPWORDS (NOVO)
    # ---------------------------
    stop_words = set(stopwords.words('portuguese'))
    tokens_filtrados = [t for t in tokens_limpos if t not in stop_words]

    # ---------------------------
    # FREQUÊNCIA
    # ---------------------------
    frequencia = Counter(tokens_filtrados)
    top_palavras = frequencia.most_common(5)

    # ---------------------------
    # RESULTADOS
    # ---------------------------
    st.subheader("📊 Resultados da Análise")

    st.write("**Total de palavras analisadas:**", len(tokens_filtrados))

    if top_palavras:
        palavra_mais_comum = top_palavras[0]
        st.write("**Palavra mais frequente:**", palavra_mais_comum)
    else:
        st.write("Nenhuma palavra relevante encontrada.")

    st.write("### Tokens processados:")
    st.write(tokens_filtrados)

    st.write("### Top palavras:")
    st.write(top_palavras)

    # ---------------------------
    # GRÁFICO (NOVO)
    # ---------------------------
    if top_palavras:
        df = pd.DataFrame(top_palavras, columns=["Palavra", "Frequência"])
        st.bar_chart(df.set_index("Palavra"))

        # EXERCICIO 3


# faça:

# Contexto

# Uma empresa de atendimento quer detectar automaticamente
#  mensagens com palavras negativas
#  para priorizar o suporte ao cliente.

# Objetivo

# Crie uma regra condicional para 
# identificar palavras como “ruim”, “péssimo” ou “erro”.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Baixa recurso de tokenização
nltk.download('punkt', quiet=True)

# Título
st.title("Exercício 3 - Detecção de Mensagens Negativas")

# Lista de palavras negativas
palavras_negativas = ["ruim", "péssimo", "horrível", "erro", "falha", "problema"]

# Entrada do usuário
texto = st.text_area(
    "Digite uma mensagem do cliente:",
    "O sistema apresentou erro e o atendimento foi ruim."
)

# Botão
if st.button("Analisar Mensagem"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Verificação de palavras negativas
    encontrados = []

    for palavra in tokens:
        if palavra in palavras_negativas:
            encontrados.append(palavra)

    # Decisão
    if len(encontrados) > 0:
        label = "⚠️ Mensagem NEGATIVA - Priorizar atendimento"
    else:
        label = "Mensagem Normal 👍"

    # Resultado
    st.write("### Resultado:")
    st.write(label)

    st.write("### Palavras negativas encontradas:")
    st.write(encontrados)

    st.write("### Tokens:")
    st.write(tokens)

     # EXERCICIO 4


# faça:

# Contexto

# Em uma análise de textos, palavras como “de”, “a”, “o”, 
# “para” não ajudam na interpretação
#  e precisam ser removidas para melhorar a análise.

# Objetivo

# Remova stopwords de um texto em português.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Downloads necessários
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Título
st.title("Exercício 4 - Remoção de Stopwords")

# Texto de entrada
texto = st.text_area(
    "Digite um texto:",
    "O aluno foi para a escola e fez a atividade com o professor."
)

# Botão
if st.button("Remover Stopwords"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Stopwords em português
    stop_words = set(stopwords.words('portuguese'))

    # Remove stopwords
    tokens_filtrados = [t for t in tokens if t.isalpha() and t not in stop_words]

    # Resultado
    st.write("### Texto original (tokens):")
    st.write(tokens)

    st.write("### Texto sem stopwords:")
    st.write(tokens_filtrados)

    # EXERCICIO 5


# faça:

# Contexto

# Uma equipe de marketing quer entender rapidamente se 
# comentários de clientes
# são positivos ou negativos com base em palavras-chave

# Objetivo

# Crie um sistema simples de classificação de sentimento usando condicionais.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 

import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)

st.title("Exercício 5 - Análise de Sentimento Dinâmica")

# Entrada livre do usuário
texto = st.text_area("Digite qualquer frase ou comentário:")

if st.button("Analisar"):

    # Proteção contra texto vazio
    if texto.strip() == "":
        st.warning("Digite algum texto para análise.")
    else:

        sia = SentimentIntensityAnalyzer()
        scores = sia.polarity_scores(texto)

        compound = scores["compound"]

        # Classificação
        if compound >= 0.05:
            label = "Positivo 😊"
        elif compound <= -0.05:
            label = "Negativo 😡"
        else:
            label = "Neutro 😐"

        # Resultado
        st.write("### Resultado da análise")
        st.write("Texto analisado:", texto)
        st.write("Label:", label)
        st.write("Score:", compound)

           # EXERCICIO 6


# faça:

# Contexto

# Um chatbot precisa identificar palavras-chave dentro de uma
#  frase para direcionar o cliente para o setor correto.

# Objetivo

# Crie uma lógica que detecte palavras como “cancelar”,
#  “erro” e “pagamento”.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Baixa recurso de tokenização
nltk.download('punkt', quiet=True)

# Título
st.title("Exercício 6 - Chatbot por Palavras-chave")

# Palavras-chave por setor
cancelamento = ["cancelar", "cancelamento", "sair"]
erro = ["erro", "problema", "bug", "falha"]
pagamento = ["pagamento", "cobrança", "boleto", "cartão"]

# Entrada do usuário
texto = st.text_area(
    "Digite sua mensagem:",
    "Quero cancelar meu plano porque deu erro no pagamento."
)

# Botão
if st.button("Analisar Mensagem", key="btn_ex6"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Detectores
    setor = "Atendimento geral"

    if any(p in tokens for p in cancelamento):
        setor = "Setor de Cancelamento"
    elif any(p in tokens for p in erro):
        setor = "Suporte Técnico (Erros)"
    elif any(p in tokens for p in pagamento):
        setor = "Financeiro / Pagamentos"

    # Resultado
    st.write("### Resultado:")
    st.write("Setor identificado:", setor)

    st.write("### Tokens:")
    st.write(tokens)

     # EXERCICIO 7


# faça:

# Contexto

# Um analista quer saber quais palavras mais aparecem 
# em reclamações de clientes para melhorar o produto.

# Objetivo

# Crie um código que identifique 
# as palavras mais frequentes em um texto de reclamação.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Downloads necessários
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Título
st.title("Exercício 7 - Frequência em Reclamações")

# Texto de entrada
texto = st.text_area(
    "Digite uma reclamação:",
    "O produto é ruim, ruim mesmo, e o atendimento foi péssimo e lento."
)

# Botão
if st.button("Analisar Reclamação"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Remove pontuação
    tokens = [t for t in tokens if t.isalpha()]

    # Remove stopwords
    stop_words = set(stopwords.words('portuguese'))
    tokens_filtrados = [t for t in tokens if t not in stop_words]

    # Frequência
    frequencia = Counter(tokens_filtrados)

    # Top palavras
    top_palavras = frequencia.most_common(5)

    # Resultado
    st.write("### Palavras mais frequentes:")
    st.write(top_palavras)

    st.write("### Tokens limpos:")
    st.write(tokens_filtrados)

    # EXERCICIO 8


# faça:

# Contexto

# Uma empresa quer classificar mensagens automaticamente em
#  “suporte técnico” 
# ou “financeiro” com base em palavras específicas.

# Objetivo

# Crie regras condicionais simples para classificar mensagens.

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Download necessário
nltk.download('punkt', quiet=True)

# Título
st.title("Exercício 8 - Classificação de Mensagens")

# Palavras-chave por categoria
suporte_tecnico = ["erro", "bug", "falha", "problema", "sistema", "travou"]
financeiro = ["pagamento", "boleto", "cobrança", "cartão", "fatura", "cobrar"]

# Entrada do usuário
texto = st.text_area(
    "Digite sua mensagem:",
    "Estou com erro no sistema e não consigo pagar o boleto."
)

# Botão
if st.button("Classificar Mensagem"):

    # Tokenização
    tokens = word_tokenize(texto.lower())

    # Categoria padrão
    categoria = "Indefinido"

    # Regras condicionais
    if any(p in tokens for p in suporte_tecnico):
        categoria = "Suporte Técnico 🖥️"
    elif any(p in tokens for p in financeiro):
        categoria = "Financeiro 💰"

    # Resultado
    st.write("### Categoria identificada:")
    st.write(categoria)

    st.write("### Tokens:")
    st.write(tokens)

      # EXERCICIO 9


# faça:

# Contexto

# Um sistema de IA precisa limpar textos removendo pontuação
#  e deixando apenas palavras relevantes para análise.

# Objetivo

# Remova pontuação e normalize um texto (letras minúsculas).

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 


import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Download necessário
nltk.download('punkt', quiet=True)

# Título
st.title("Exercício 9 - Limpeza e Normalização de Texto")

# Entrada do usuário
texto = st.text_area(
    "Digite um texto:",
    "O Produto é BOM!!!, mas o Atendimento foi RUIM..."
)

# Botão
if st.button("Limpar Texto"):

    # Normalização (minúsculas)
    texto_normalizado = texto.lower()

    # Tokenização
    tokens = word_tokenize(texto_normalizado)

    # Remove pontuação e caracteres não alfabéticos
    tokens_limpos = [t for t in tokens if t.isalpha()]

    # Resultado
    st.write("### Texto original:")
    st.write(texto)

    st.write("### Tokens limpos:")
    st.write(tokens_limpos)

    # EXERCICIO 10


# faça:

# Contexto

# Uma empresa quer entender o conteúdo de avaliações de 
# produtos para identificar se os clientes
#  estão satisfeitos ou insatisfeitos sem leitura manual.

# Objetivo

# Combine tokenização + 
# condicional para analisar sentimento básico de um texto

# Estilo

# Código simples e linear, sem funções desnecessárias.
#  Só o essencial para funcionar.

# Tom

# Direto, com comentários curtos explicando cada bloco.

# Resultado

# Um único `app.py` com:

# - `nltk.download('vader_lexicon')`
# - `SentimentIntensityAnalyzer`
# - `st.text_area` para entrada
# - `st.button` para analisar
# - `st.write` mostrando o label e o score
# - `requirements.txt` com `streamlit` e `nltk` 

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Downloads necessários
nltk.download('punkt', quiet=True)
nltk.download('vader_lexicon', quiet=True)

# Título
st.title("Exercício 10 - Análise de Sentimento com NLP")

# Entrada do usuário
texto = st.text_area(
    "Digite uma avaliação de produto:",
    "O produto é ótimo, mas o atendimento foi ruim."
)

# Botão
if st.button("Analisar", key="btn_ex10"):

    # -----------------------
    # TOKENIZAÇÃO
    # -----------------------
    tokens = word_tokenize(texto.lower())

    # -----------------------
    # ANÁLISE DE SENTIMENTO
    # -----------------------
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(texto)

    compound = scores["compound"]

    # Classificação por regra
    if compound >= 0.05:
        label = "Satisfeito 😊"
    elif compound <= -0.05:
        label = "Insatisfeito 😡"
    else:
        label = "Neutro 😐"

    # -----------------------
    # RESULTADO
    # -----------------------
    st.write("### Resultado da análise")
    st.write("Texto analisado:", texto)
    st.write("Tokens:", tokens)
    st.write("Label:", label)
    st.write("Score:", compound)