# pip install mlrose --no-deps
import six 
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

produtos = [
    ('Refrigerador A', 0.751, 999.90),
    ('Celular', 0.0000899, 2911.12),
    ('TV 55', 0.400, 4346.99),
    ('TV 50', 0.290, 3999.90),
    ('TV 42', 0.200, 2999.00),
    ('Notebook A', 0.00350, 2499.90),
    ('Ventilador', 0.496, 199.90),
    ('Microondas A', 0.0424, 308.66),
    ('Microondas B', 0.0544, 429.90),
    ('Microondas C', 0.0319, 299.29),
    ('Refrigerador B', 0.635, 849.00),
    ('Refrigerador C', 0.870, 1199.89),
    ('Notebook B', 0.498, 1999.90),
    ('Notebook C', 0.527, 3999.00)
]

espaco_disponivel = 3

def fitness_function(solucao):

    soma_produtos = 0
    custo = 0

    for i in range(len(solucao)):
        if solucao[i] == 1: 
            custo += produtos[i][2]
            soma_produtos += produtos[i][1]

    if soma_produtos > espaco_disponivel:
        custo = 1

    return custo

def imprimir_solucao(solucao):
    for i in range(len(solucao)):
        if solucao[i] == 1:
            print('%s - %s' % (produtos[i][0], produtos[i][2]))

fitness_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])    

fitness = mlrose.CustomFitness(fitness_function)

problema = mlrose.DiscreteOpt(length=14,fitness_fn=fitness,maximize=True, max_val=2)

melhor_solucao, melhor_custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2)
imprimir_solucao(melhor_solucao)
print(melhor_solucao, melhor_custo)
