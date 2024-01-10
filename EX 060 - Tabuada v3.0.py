print('-'*10, end='')
print(' PROGRAMA DA TABUADA ', end='')
print('-'*10)

while True:
    print(' ')
    num = int(input('Quer ver a tabuada de qual valor? '))

    if num < 0:
        break

    for c in range(0, 11):
        print(f'{num} x {c} = {num * c}')
    print('*-' * 10)

print('PROGRAMA ENCERRADO. Volte sempre!')
