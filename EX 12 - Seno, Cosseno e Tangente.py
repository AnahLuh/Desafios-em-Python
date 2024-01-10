# Entrada
import math
num = float(input('Digite o valor de um ângulo: '))

print('O ângulo de {} tem \n SENO de {}, \n COSSENO de {} e \n TANGENTE de {}.'.format(num, math.sin(math.radians(num)), math.cos(math.radians(num)), math.tan(math.radians(num))))

# É bom transformar pra radianos os ângulos
