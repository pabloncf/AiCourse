import bs4 as bs
import urllib.request
import nltk
import spacy

# ================================ Stemização ==================================
pln = spacy.load("pt_core_news_sm") # Defininfo portugues

documento = pln('Estou aprendendo processamento de linguagem natural na Horanda') # Texto exemplo

nltk.download('rslp')

print("=====================")

stemmer = nltk.stem.RSLPStemmer()
for token in documento: # Na stemização ele vai pegar o corpo da palavra
    print(token.text, token.lemma_, stemmer.stem(token.text))

print("=====================")