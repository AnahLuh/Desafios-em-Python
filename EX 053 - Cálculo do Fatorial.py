n = int(input('Digite um número: '))
c = n
f = 1 # Multiplicação tem que ser 1 e não 0
print(f'Calculando... {n}! = ', end= '')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else '=', end = ' ') # Vai multiplicando e no final coloca um igual.
    f *= c
    c -= 1
print(f'{f}')
