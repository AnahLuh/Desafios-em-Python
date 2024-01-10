from random import randint
from time import sleep
numtemp = []
numprinc = numtemp[:]


def sorteia(qnt, min, max): # Quantos números quer sortear e qual o intervalo que eles devem ser sorteados(min, max).
    for c in range(0, qnt):
        numtemp.append(randint(min, max))

    print(f'\033[1;32m( ', end='')
    for i in numtemp:
        print(f'{i}', end= ' ')
    print(')')

    soma = 0
    qntpares = 0
    for i in numtemp:
        if i % 2 == 0:
            qntpares += 1
            soma += i
    sleep(0.5)
    print(f'\033[0;0m\nForam sorteados {qntpares} números pares! A soma deles é igual a {soma}.')

    numprinc.append(numtemp[:])
    numtemp.clear()

print('----- SORTEADOR -----')
print()
qnt = int(input('Quantos números você deseja sortear? '))
if qnt == 0:
    print('ERRO! Digite novamente!')
    qnt = int(input('Quantos números você deseja sortear? '))
min = int(input('Valor mínimo a ser sorteado: '))
max = int(input('Valor máximo a ser sorteado: '))
print(f'Sorteando os {qnt} valores...')

sleep(1)
sorteia(qnt, min, max)

while True:
    repetir_mesmos_valores = str(input('\n Deseja sortear novos números com os mesmos parâmetros?[S/N] ')).strip()[0].upper()
    while repetir_mesmos_valores not in 'SN':
        print('ERRO!', end= ' ')
        repetir_mesmos_valores = str(input(' Deseja sortear novos números com os mesmos parâmetros?[S/N] ')).strip()[0].upper()
    if repetir_mesmos_valores in 'N':
        nova_repeticao = str(input('  Deseja um novo sorteio com novos parâmetros?[S/N] ')).strip()[0].upper()
        while repetir_mesmos_valores not in 'SN':
            print('ERRO!', end=' ')
            repetir_mesmos_valores = str(input('  Deseja um novo sorteio com novos parâmetros?[S/N] ')).strip()[0].upper()
        if nova_repeticao in 'N':
            break
        elif nova_repeticao in 'S':
            qnt = int(input('Quantos números você deseja sortear? '))
            if qnt == 0:
                print('ERRO! Digite novamente!')
                qnt = int(input('Quantos números você deseja sortear? '))
            min = int(input('Valor mínimo a ser sorteado: '))
            max = int(input('Valor máximo a ser sorteado: '))



    sleep(1)
    sorteia(qnt, min, max)

print('VOLTE SEMPRE!')




