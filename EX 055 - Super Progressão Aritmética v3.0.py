
print('GERADOR DE PA')
print('-='*8)

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeirotermo
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} →'.format(termo), end = ' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))


