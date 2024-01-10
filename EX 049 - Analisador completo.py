# Variáveis acumuladas

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
numhomem = 0

for c in range(1, 5):
    print('-'*10, end=' ')
    print('{}ª PESSOA'.format(c), end=' ')
    print('-'*10)
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]:')).strip()
    somaidade += idade

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
    if sexo in 'Mm':
        numhomem += 1

mediaidade = (somaidade / 4)

print('A média de idade do grupo é de {} anos.'.format(mediaidade))

if numhomem != 0: # Se não tiver nenhum homem, esse print não aparece.
    print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))

print('Ao todo há {} mulheres com menos de 20 anos.'.format(totalmulher20))



