soma = 0
cont = 0

for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c # soma = soma + c
        cont += 1 # cont = cont + 1
print('A soma dos {} valores solicitados é de {}.'.format(cont, soma))

