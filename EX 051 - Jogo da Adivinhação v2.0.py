from random import randint
computador = randint(0,10)
print('-='*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-='*20)

jogador = int(input('Em que número eu pensei? '))
if jogador < computador:
    print('Mais..')
if jogador > computador:
    print('Menos...')
tentativas = 0

while jogador != computador:
    print(f'HAHAHA! Eu venci! Pensei no número {computador}.')
    jogador = int(input('Te dou mais uma chance. Em que número eu pensei? '))
    tentativas += 1
    if jogador < computador:
        print('Mais..')
    if jogador > computador:
        print('Menos...')

if jogador == computador:
    print('Oh não! Fui vencido!')

print(f'Acertou com {tentativas + 1} tentativas. PARABÉNS!')


