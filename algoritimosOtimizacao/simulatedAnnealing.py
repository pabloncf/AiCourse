# pip install mlrose --no-deps
import six 
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

pessoas = [
    ('Lisboa', 'LIS'),
    ('Madrid','MAD'),
    ('Paris','CDG'),
    ('Dublin', 'DUB'),
    ('Bruxelas', 'BRU'),
    ('Londres','LHR')
]

destino = 'FCO'

voos = {}
for linha in open('C:/Users/pablo/OneDrive/Documentos/BackendJFPB/aulasUdemy/algoritimosOtimizacao/flights.txt'):
    #print(linha.split(','))
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem,destino)].append((saida, chegada, int(preco)))

agenda = [1,7 ,3,1, 1,1 ,6,3 ,2,4 ,5,3]

def fitness_function(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem,destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
    
    return total_preco

def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        nome = pessoas[i][0]
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem,destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome,origem,ida[0],ida[1],ida[2], volta[0], volta[1], volta[2]))
    print('Preço total: ', total_preco)

fitness_function(agenda)

fitness = mlrose.CustomFitness(fitness_function)

problema = mlrose.DiscreteOpt(length=12,fitness_fn=fitness, maximize=False, max_val=10)

melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema, schedule=mlrose.decay.GeomDecay(init_temp=10000), random_state=1)

#Solução para não precisar ficar fazer 1 por 1 (made by me)
'''initTemp = 10000
for i in range(initTemp):
    i += 1
    melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema, schedule=mlrose.decay.GeomDecay(init_temp=i), random_state=1)
    print(melhor_solucao, melhor_custo)'''

imprimir_voos(melhor_solucao)


