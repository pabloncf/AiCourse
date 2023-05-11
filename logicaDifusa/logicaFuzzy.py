import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitável', 'ótimo'])

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 8])
gorjeta['média'] = fuzz.trimf(gorjeta.universe, [2, 10, 18])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [12, 20, 20])

gorjeta.view()

regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitável'], gorjeta['média'])
regra3 = ctrl.Rule(servico['ótimo'] | qualidade['saborosa'], gorjeta['alta'])

# SISTEMA DE CONTROLE
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])

sistema = ctrl.ControlSystemSimulation(sistema_controle)
sistema.input['qualidade'] = 8.5
sistema.input['servico'] = 6.5
sistema.compute()

print(sistema.output['gorjeta'])