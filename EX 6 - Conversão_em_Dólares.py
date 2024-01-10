# Setando as variáveis

reais = float(input('Quanto de dinheiro você tem na carteira?'))
dolares = reais/3.27 #Conversão de R$3.27 = U$1.00

# Resultado com aproximação de duas casas decimais

print('Com {} reais você pode comprar {:.2f} dólares.'.format(reais, dolares))
