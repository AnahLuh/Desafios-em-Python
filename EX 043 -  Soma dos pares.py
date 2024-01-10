soma = 0
cont = 0

for c in range(0, 6):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        soma = soma + x
        cont += 1
print('A soma dos {} números pares é {}.'.format(cont, soma))