lista = list()
c = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    c += 1

    opcao = str(input('Deseja continuar [S/N]? ')).strip()[0].upper()
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).strip()[0].upper()
    if opcao in 'N':
        break

print()
print(f'Você digitou {c} elementos nesta lista.')

lista.sort(reverse=True)
print('Os valores em ordem decrescente são:')
print(lista)

if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
