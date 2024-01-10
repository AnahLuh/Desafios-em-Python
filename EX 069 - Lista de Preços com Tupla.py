print('='*30)
print(f'{"TIENDA DO LOLIPOPI":^30}')
print('='*30)

lista = ('Galletas', '2',
         'Agua', '14',
         'Huevo', '40',
         'Manzana', '20',
         'Leche', '20',
         'Elote Entero', '25')

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'MX${lista[pos]:>1}')


