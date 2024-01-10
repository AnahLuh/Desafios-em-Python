
d = float(input('Qual a distância da viagem? '))

p1 = d * 0.5
p2 = d * 0.45

if 200 >= d:
    print('O preço da passagem será de R${}.'.format(p1))
else:
    print('O preço da passagem será de R${}.'.format(p2))
