paises = ('Estados Unidos', 'China', 'Japão',
          'Alemanha', 'Reino Unido', 'França',
          'Índia', 'Itália', 'Brasil', 'Canadá')

print('Os países com os 5 maiores PIBs do mundo são:')

c = 0
for n in paises[:5]:
    c += 1
    print(f'{c}º - {n}')

print(' ')

print('Os últimos 4 países desta lista são:')

x = 0
for p in paises[6:]:
    x += 1
    print(f'{x + 6}º - {p}')

print(' ')

print(f'O Brasil está na {paises.index("Brasil") + 1}ª posição.')