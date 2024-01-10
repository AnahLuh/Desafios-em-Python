peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / altura ** 2

print('O seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5: # ABAIXO DO PESO
    print('CUIDADO! Você está ABAIXO do seu peso ideal!')
elif 18.5 <= imc < 25: # PESO IDEAL
    print('PARABÉNS! Você está no peso ideal!')
elif 25 <= imc < 30: # SOBREPESO
    print('Cuidado! Você está com SOBREPESO.')
elif 30 <= imc < 40: # OBESIDADE
    print('CUIDADO! Você está com OBESIDADE!')
else:
    print('MUITO CUIDADO! Você está com OBESIDADE MÓRBIDA!')