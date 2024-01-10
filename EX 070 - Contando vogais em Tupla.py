palavras = ('eu', 'adoro', 'doces')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end= ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;31m{letra}\033[m', end=' ')
    print('.')