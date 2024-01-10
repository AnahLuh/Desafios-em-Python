# Entrada

preco = float(input('Qual o preço do produto?'))

# Desconto no produto

desconto = preco*0.05 # Desconto de 5%
precofinal = preco - desconto

#Saída

print('Com o desconto, você pagará {}.'.format(precofinal))
