# Entradas
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('A média do aluno foi de {}.'.format(media))
    print('Ele foi REPROVADO!')
elif 5.0 <= media <= 6.9:
    print('A média do aluno foi de {}.'.format(media))
    print('Ele está de RECUPERAÇÃO!')
else:
    print('A média do aluno foi de {}.'.format(media))
    print('Ele foi APROVADO!')