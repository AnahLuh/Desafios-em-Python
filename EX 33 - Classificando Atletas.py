from datetime import date
ano = int(input('Ano de nascimento do Atleta: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('Um atleta com {} anos é da categoria MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('Um atleta com {} anos é da categoria INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('Um atleta com {} anos é da categoria JUNIOR.'.format(idade))
elif 19 < idade <= 25:
    print('Um atleta com {} anos é da categoria SÊNIOR.'.format(idade))
else:
    print('Um atleta com {} anos é da categoria MASTER.'.format(idade))