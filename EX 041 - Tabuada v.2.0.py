num = int(input('Digite um número inteiro: '))

print('-'*10, end= ' ')
print('TABUADA DO {}'.format(num), end= ' ')
print('-'*10)

for c in range (0, 11):
    print('{} x {} = {}'.format(num, c, (num * c)))

print('-'*34)