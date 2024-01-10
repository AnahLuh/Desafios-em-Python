from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        for c in range(inicio, fim - 1, passo):

            print(f'{c}', end= ' ')
            sleep(0.5)
        print('FIM!')

    if passo > 0:
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end = ' ')
            sleep(0.5)
        print('FIM!')


print('~~~~ VAMOS CONTAR DE 1 A 10 DE 1 EM 1? ~~~~')
print()
contador(1, 10, 1)
print()

sleep(1)

print('~~~~ VAMOS CONTAR DE 10 A 0 DE 2 EM 2? ~~~~')
print()
contador(10, 0, -2)
print()
print('-'*20)
sleep(1)

print('AGORA É A SUA VEZ!')

inicio = int(input('Em qual número devo começar? '))
fim = int(input('Em qual número devo terminar? '))
passo = int(input('Em qual passo devo contar? '))

print(f'Está bem.. Vou contar de {inicio} até {fim} ao passo de {passo}.')
sleep(1)
contador(inicio, fim, passo)




