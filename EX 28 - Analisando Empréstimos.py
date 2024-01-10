# Entradas

casa = float(input('Qual o valor da casa? '))
salarios = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos deseja-se financiar? '))

prestacao = casa / (anos * 12) # Em meses

x = prestacao / salarios # Relação da prestação com o salário

if x <= 0.3:
    print('Para pagar uma casa de R${} por {} anos a prestação será de {:.2f}.'.format(casa, anos, prestacao))
    print('Portanto o seu empréstimo foi CEDIDO!')
else:
    print('Para pagar uma casa de R${} por {} anos a prestação será de {:.2f}.'.format(casa, anos, prestacao))
    print('Portanto o seu empréstimo foi NEGADO!')