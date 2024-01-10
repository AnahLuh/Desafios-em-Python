
s = float(input('Qual o salário? '))

n1 = s + (s * 0.10)
n2 = s + (s * 0.15)

if s <= 1250:
    print('O seu salário com aumento será igual a {}.'.format(n2))
else:
    print('O seu salário com aumento será igual a {}.'.format(n1))
