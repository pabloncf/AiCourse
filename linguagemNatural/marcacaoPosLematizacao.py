import bs4 as bs
import urllib.request
import nltk
import spacy

# ============================== Lematização ===============================

pln = spacy.load("pt_core_news_sm") # Defininfo portugues

documento = pln('Estou aprendendo processamento de linguagem natural na Horanda') # Texto exemplo

for token in documento: #fazendo a classificação das palavras. Exemplo: pronome, adjetivo, verbo, etc
    print(token.text, token.pos_)

print("=====================")

for token in documento: # Fazendo a transformação de palavras derivadas em apenas uma para facilitar o aprendizado da maquina
    print(token.text, token.lemma_)

print("=====================")





