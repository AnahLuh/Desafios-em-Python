cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end= '')
    print(f'O número digitado foi \033[1;31m{cont[num]}.\n\033[m')

    opcao = str(input('Deseja continuar? ')).strip()[0].upper()

    while opcao not in 'SsNn':
        opcao = str(input('Deseja continuar? ')).strip()[0].upper()

    if opcao == 'N':
        break

print('Obrigado, volte sempre!')