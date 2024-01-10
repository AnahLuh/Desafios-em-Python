print('='*8 , end = ' ')
print('TIENDA LOLIPOPI', end = ' ')
print('='*8)

preco = float(input('Qual o preço do produto? '))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual a opção? '))

if opcao == 1:
    desconto = preco * 0.1
    print('O seu desconto é de R${}, ou seja, você pagará R${}.'.format(desconto, (preco - desconto)))
elif opcao == 2:
    desconto1 = preco * 0.05
    print('O seu desconto é de R${}, ou seja, você pagará R${}.'.format(desconto1, (preco - desconto1)))
elif opcao == 3:
    print('Você não terá desconto. Por isso, continuará pagando R${}, em duas parcelas de R${} cada SEM JUROS.'.format(preco, preco / 2))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas? '))
    precofinal = preco + (preco * 0.2)
    print('Com os JUROS você pagará R${} em {} parcelas de R${}. '.format(precofinal, parcelas, ( precofinal / parcelas) ))
else:
    print('Opção inválida! Tente novamente.')