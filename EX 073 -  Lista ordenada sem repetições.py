lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0:
        lista.append(n)
        print('Valor adicionado ao final da lista...')


    if c == 1:
        if n < lista[0]:
            lista.insert(0, n)
            print('Valor adicionado ao começo da lista...')
        if n > lista[0]:
            lista.insert(1, n)
            print('Valor adicionado na posição 2.')

    if c == 2:
        if n < lista[1]:
            lista.insert(0, n)
            print('Valor adicionado ao começo da lista...')
        if n > lista[1]:
            lista.insert(2, n)
            print('Valor adicionado na posição 3.')

    if c == 3:
        if n < lista[2]:
            lista.insert(0, n)
            print('Valor adicionado ao começo da lista...')
        if n > lista[2]:
            lista.insert(3, n)
            print('Valor adicionado na posição 4.')

    if c == 4:
        if n < lista[3]:
            lista.insert(0, n)
            print('Valor adicionado ao começo da lista...')
        if n > lista[3]:
            lista.insert(4, n)
            print('Valor adicionado na posição 5.')



print('Os valores digitados foram:')
print(lista)
