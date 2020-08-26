# Author: Carolina Barbosa
import constants as c
import numpy as np

import constants2 as c2 # Exemplo visto em sala # Mudar recompensas pra testar

# Matriz de estados
# 2 5 8 11
# 1 4 7 10
# 0 3 6 9

# r1 = -0.4
# r2 = -0.04
# r3 = -0.0004

# Atualizar os valores da funcaoo de utilidade dos estados
def update_value(rw, value):
    value_aux = np.zeros(12)

    for i in range(12):
        v_up = sum(c.T_up[i] * value)
        v_down = sum(c.T_down[i] * value)
        v_left = sum(c.T_left[i] * value)
        v_right = sum(c.T_right[i] * value)

        value_aux[i] = round(rw[i] + max(v_up,v_down,v_left,v_right), 4)

    print('[' + str(value_aux[2]) + ' ' + str(value_aux[5]) + ' ' + str(value_aux[8]) + ' ' + str(value_aux[11]))
    print(str(value_aux[1]) + ' ' + str(value_aux[4]) + ' ' + str(value_aux[7]) + ' ' + str(value_aux[10]))
    print(str(value_aux[0]) + ' ' + str(value_aux[3]) + ' ' + str(value_aux[6]) + ' ' + str(value_aux[9]) + ']\n')

    return value_aux

 # Calcular a politica a partir das utilidades 
def return_policy(value):
    actions = ['UP','DW','LF','RG']

    policy = np.array(['  ']*12)
    policy[10] = '-1'
    policy[11] = '1'

    for i in range(10):
        v_up = sum(c.T_up[i] * value)
        v_down = sum(c.T_down[i] * value)
        v_left = sum(c.T_left[i] * value)
        v_right = sum(c.T_right[i] * value)

        policy[i] = actions[np.argmax(np.array([v_up, v_down, v_left, v_right]))]

    print(policy[2] + ' ' + policy[5] + ' ' + policy[8] + ' ' + policy[11])
    print(policy[1] + ' ' + policy[4] + ' ' + policy[7] + ' ' + policy[10])
    print(policy[0] + ' ' + policy[3] + ' ' + policy[6] + ' ' + policy[9] + '\n')
    
def main():
    r = input("Digite o valor de r (valor fixo) para todos estados não terminais:\n")

    # Inicializando recompensas
    rw = np.array([float(r)]*12)

    # Exemplo visto em sala
    # rw[4] = 0
 
    rw[4] = -0.5
    rw[9] = 0.2
    rw[10] = -1
    rw[11] = 1

    # Inicializando valores de utilidade com zero
    value = np.zeros(12)

    # Aplicando as equacoes de Bellman por 100 iteracoes
    for i in range(100):
        value = update_value(rw, value)

    return_policy(value)

if __name__ == '__main__':
	main()