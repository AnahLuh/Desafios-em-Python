

num = int(input('Digite um número inteiro entre 0 e 9999: '))

m = num // 1000 % 10 # Pega o número, faz uma divisão inteira e depois divide mostrando o resto da divisão
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print('O número {} tem'.format(num))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezenas: {}'.format(d))
print('Unidades: {}.'.format(u))
