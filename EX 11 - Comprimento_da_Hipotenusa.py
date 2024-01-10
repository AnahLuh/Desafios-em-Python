# Entradas
import math

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hip = math.sqrt((co**2 + ca**2)) # Outra forma seria (   )**(1/2)

# Saída
print('A hipotenusa deste triângulo retângulo vale {:.3f}.'.format(hip))

''' Outra forma de solução:

from math import hypot

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hip = hypot(co, ca)

print('A hipotenusa deste triângulo retângulo vale {:.3f}.'.format(hip))'''
