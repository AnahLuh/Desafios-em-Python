temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    opcao = str(input('Deseja continuar? [S/N]')).strip()[0].upper()
    if opcao in 'N':
        break

print(f'Qnt = {len(princ)}')
print(f'Elementos = {princ}')
print(f'MAIOR PESO = {maior}')
print(f'MENOR PESO = {menor}')