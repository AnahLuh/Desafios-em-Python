import random
import time

n = random.randint(0, 5) # Computador escolhe um número entre 0 e 5

print('-=--'*10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--'*10)

num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')

time.sleep(3) # Dar um delay no próximo print

if num == n:
    print('Oh não! Fui vencido! Parabéns!')
else:
    print('Hahaha, eu ganhei! Pensei no número {}.'.format(n))
