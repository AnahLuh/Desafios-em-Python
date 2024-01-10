print(' ')
print('-*'*7, end='')
print('  ÍMPAR OU PAR?  ', end= '')
print('-*'*7)

from time import sleep # Pra fazer o tempinho da música

from random import randint
# computador = randint(0,10) -> Se tu faz isso fora do WHILE, o computador sempre vai considerar o mesmo valor para
# todo o programa até que vc perca!

n = 0
resultado = 'P'

while True: # Looping infinito
    print(' ')
    jogador = int(input('Digite um número [0 a 10]: '))
    computador = randint(0, 10)
    aposta = str(input('Ímpar ou par [I/P]? ')).strip()[0].upper()

    while aposta not in 'IiPp':
        aposta = str(input('Ímpar ou par [I/P]? ')).strip()[0].upper()
    print(' ')

    print('ÍMPAR...', end = '')
    sleep(0.5)
    print(' ou ...', end = '')
    sleep(0.5)
    print(' PAR!')

    print(f'Você jogou {jogador} e o computador jogou {computador}.')

    total = jogador + computador
    if total % 2 == 0:
        print(f'O TOTAL foi de {total}. DEU \033[1;31mPAR!')
        if resultado == aposta:
            print('\n\033[mOH NÃO! Fui vencido! PARABÉNS!')
            n += 1

        else:
            print('\n\033[mHAHAHA! EU GANHEI!')
            break

    if total % 2 != 0:
        print(f'O TOTAL foi de {total}. DEU \033[1;31mÍMPAR!')
        if resultado != aposta:

            print('\n\033[mOH NÃO! Fui vencido! PARABÉNS!')
            n += 1

        else:
            print('\n\033[mHAHAHA! EU GANHEI!')
            break

if n == 0:
    print('GAMEOVER! Você não ganhou nenhuma vez!')
elif n == 1:
    print('GAMEOVER! Você ganhou uma vez!')
else:
    print(f'GAMEOVER! Você ganhou {n} vezes!')


