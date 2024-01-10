n = 0 # Maiores de 18 anos cadastrados
h = 0 # Qnt de homens cadastrados
m = 0 # Mulheres menores de 20 anos cadastradas
x = 0 # Quantas vezes aconteceu o looping

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    continuacao = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    while continuacao not in 'SsNn':
        continuacao = str(input('Quer continuar [S/N]? ')).upper().strip()[0]

    if idade > 18:
        n += 1

    if sexo in 'Mn':
        h += 1

    if idade < 20 and sexo in 'Ff':
        m += 1

    if continuacao in 'Nn':
        break

    x += 1 # Prestar atenção na posição deste contador. Caso ele venha depois do break, ele n vai contar a última ocorrência.

if x == 0:
    print(f'Foi cadastrada UMA pessoa:')
else:
    print(f'Foram cadastradas {x + 1} pessoas.')

if x == 0: # Se o usuário cadastra apenas uma pessoa no programa.
    if n == 0:
        print('A pessoa cadastrada é MENOR de 18 anos.')
    elif n == 1:
        print('A pessoa cadastrada é MAIOR de 18 anos.')

    if h == 0:
        print('A pessoa cadastrada é MULHER.')
    elif h == 1:
        print('A pessoa cadastrada é HOMEM.')

    if m == 0:
        print('Essa mulher cadastrada é MAIOR de 20 anos.')
    elif m == 1:
        print('Essa mulher cadastrada é MENOR de 20 anos.')

else: # Se o usuário cadastra duas ou mais pessoas no programa.
    if n == 1:
        print(f'Foi cadastrada UMA pessoa MAIOR de 18 anos.')
    else:
        print(f'Foram cadastradas {n} pessoas MAIORES de 18 anos.')

    if h == 1:
        print(f'Foi cadastrado UM homem. ')
    else:
        print(f'Foram cadastrados {h} homens.')

    if m == 1:
        print(f'Foi cadastrada UMA mulher com menos de 20 anos.')
    else:
        print(f'Foram cadastradas {m} mulheres com menos de 20 anos.')
