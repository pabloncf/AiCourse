import numpy as np

class Vertice:
    def __init__(self,rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado =  False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

        def adiciona_adjacentes(self,adjacentes):
            self.adjacentes.append(adjacentes)
        
        def mostra_adjacentes(self):
            for i in self.adjacentes:
                print(i.vertice.rotulo, i.custo)

class Adjacente:
    def __init__(self,vertice,custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo

class Grafo:
    porto_uniao = Vertice('Porto União', 203)
    paulo_frontin = Vertice('Paulo Frontin', 172)
    canoinhas = Vertice('Canoinhas', 141)
    tres_barras = Vertice('Três Barras', 131)
    sao_mateus = Vertice('São Mateus do Sul', 123)
    curitiba = Vertice('Curitiba', 0)
    palmeira = Vertice('Palmeira', 59)
    mafra = Vertice('Mafra', 94)
    campo_largo = Vertice('Campo Largo', 27)
    balsa_nova = Vertice('Balsa Nova', 41)
    lapa = Vertice('Lapa', 74)
    tijucas_sul = Vertice('Tijucas do Sul', 56)
    araucaria = Vertice('Araucaria',23)
    sao_jose_pinhais = Vertice('São José dos Pinhais',13)
    contenda = Vertice('Contenda',39)

    