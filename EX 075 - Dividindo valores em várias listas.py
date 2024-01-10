num = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    num.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 != 0:
        impares.append(valor)

    opcao = str(input('Quer continuar [S/N]? ')).strip()[0].upper()
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]? ')).strip()[0].upper()
    if opcao in 'N':
        break

print('-'*15)

num.sort()
print(f'A lista completa é {num}.')
pares.sort()
print(f'A lista de pares é {pares}.')
impares.sort()
print(f'A lista de ímpares é {impares}.')
