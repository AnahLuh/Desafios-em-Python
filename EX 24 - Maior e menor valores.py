
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a < b and a < c:
    print('O menor valor é {}.'.format(a))
if b < a and b < c:
    print('O menor valor é {}.'.format(b))
if c < a and c < b:
    print('O menor valor é {}.'format(c))

if a > b and a > c:
    print('O maior valor é ().'.format(a))
if b > a and b > c:
    print('O maior valor é {}.'.format(b))
if c > a and c > b:
    print('O maior valor é {}.'.format(c))
