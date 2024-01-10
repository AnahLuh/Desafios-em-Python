from random import randint

print('Os valores sorteados foram:')

computador = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for n in computador:
    print(f'{n}', end= ' ')

print(f'\nO maior valor foi {max(computador)} e o menor valor foi {min(computador)}.')

# Outra opção é ordenar a lista e printar o elemento selecionado.



