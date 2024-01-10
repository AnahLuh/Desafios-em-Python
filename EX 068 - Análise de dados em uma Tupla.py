num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))

print(f'Você digitou os números {num}.')

if num.count(9) == 0:
    print('O número 9 não apareceu nenhuma vez.')
elif num.count(9) == 1:
    print('O número 9 apareceu UMA vez.')
else:
    print(f'O número 9 apareceu {num.count(9)} vezes.')

if num.count(3) == 0:
    print('Você não digitou nenhum valor 3.')
elif num.count(3) == 1:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print(f'O primeiro valor 3 digitado apareceu na {num.index(3) + 1}ª posição.')

print('Os valores pares foram: ')
for c in num:
    if c % 2 == 0:
        print(f'{c}', end= ' ')