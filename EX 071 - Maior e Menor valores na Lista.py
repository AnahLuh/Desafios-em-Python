lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

print('=' * 20)
print('Os valores digitados foram:')
print(lista)
print()

print(f'O maior valor foi {max(lista)} nas posições... ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{v}...', end='')

print(f'\nO menor valor foi {min(lista)} nas posições... ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{v}...', end='')