
lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar a lista..')

    opcao = str(input('Deseja continuar [S/N]? ')).strip()[0].upper()
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).strip()[0].upper()
    if opcao in 'N':
        break

print('Os valores digitados foram:')
lista.sort()
print(lista)
