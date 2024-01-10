# Importando o módulo math

import math

# Entrada
num = float(input('Digite um número: '))

arredondado = math.trunc(num)

# Saída

print('A porção inteira de {} é {}.'.format(num, arredondado))

''' Outra opção para resolução deste problema seria:

num = float(input('Digite um valor: '))
print('A porção inteira de {} é {}.'.format(num, int(num)))'''
