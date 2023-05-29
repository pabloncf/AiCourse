import bs4 as bs
import urllib.request
import nltk
import spacy

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