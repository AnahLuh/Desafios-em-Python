
v = float(input('Velocidade do carro: '))
m = int(v - 80) * 7

if v >= 81:
    print('Você foi MULTADO! Deve pagar RS {}.'.format(m))
else:
    print('Parabéns! Você não utrapassou a velocidade máxima.')
