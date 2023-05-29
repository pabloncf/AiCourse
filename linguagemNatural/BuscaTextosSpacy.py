import bs4 as bs
import urllib.request
import nltk
import spacy
from spacy.matcher import PhraseMatcher


# === Carregando dados e tratando para Exemplo ===

dados = urllib.request.urlopen("https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial")

dados = dados.read() # Pega o HTML da pagina

dados_html = bs.BeautifulSoup(dados, 'lxml') # Organiza e apresenta o html da pagina

# print(dados_html)

paragrafos = dados_html.find_all('p') # Buscando apenas as tags <p>

# Fazendo um for para tratar o texto selecionado acima no site e jogando para apenas uma variável

conteudo = ''
for p in paragrafos:
    conteudo += p.text

conteudo = conteudo.lower()

# print(conteudo)

# === Busca de textos com spaCy ===

pln = spacy.load('pt_core_news_sm')

string = str(input("Digite a palavra que deseja procurar: "))
token_pesquisa = pln(string)

matcher = PhraseMatcher(pln.vocab)
matcher.add('SEARCH', None, token_pesquisa)

doc = pln(conteudo)
matches = matcher(doc)

# print(matches) # Localização das palavras no texto

# print(doc[3351:3352+5]) # Ele mostra a palavra + 5 palavras perto dela

# Visualizando o paragrafo ao redor da Palavra solicitada

numero_palavras = 50
doc = pln(conteudo)
matches = matcher(doc)
texto = ''

for i in matches:
    inicio = i[1] - numero_palavras
    if inicio < 0:
        inicio = 0
    texto += str(doc[inicio:i[2] + numero_palavras])

print(f"Palavras encontradas: {len(matches)}")
print(f"===============================")
print(f"... {texto} ...")
