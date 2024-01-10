print('-'*25)
x = 'LOJA SUPER ATACADÃO'
print('{:^25}'.format(x))
print('-'*25)
total = 0
n = 0
cont = 0
menor = 0
barato = ' '

while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$ '))
    continuar = str(input('Você deseja adicionar mais alguma coisa no carrinho [S/N]? ')).strip()[0].upper()
    while continuar not in 'SsNn':
        continuar = str(input('Você deseja adicionar mais alguma coisa no carrinho [S/N]? ')).strip()[0].upper()
    cont += 1
    total += preco

    if preco > 1000:
        n += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    if continuar in 'Nn':
        break

print('----- FIM DO PROGRAMA -----')

print(f'Você gastou R${total} no total!')
print(f'Comprou {n} produtos que custavam mais de R$1000,00!')
print(f'O produto mais barato foi o/a {barato} que custou R${menor}.')