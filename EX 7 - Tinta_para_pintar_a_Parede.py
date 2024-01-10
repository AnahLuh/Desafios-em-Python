# Setando as variáveis

largura = float(input('Qual a largura da parede em metros?'))
altura = float(input('Qual a altura da parede em metros?'))

area = largura*altura

tinta = area/2 #1L de tinta pinta 2m2

# Resultados

print('Você precisa de {}L de tinta para pintar essa parede.'.format(tinta))

