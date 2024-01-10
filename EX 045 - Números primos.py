num = int(input('Digite um número: '))
tot = 0 # Vai contar quantos numeros dividem num
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;32m', end=' ') # Código de cor verde
        tot += 1
    else:
        print('\033[1;37m', end='') # Código de cor cinza claro
    print('{}'.format(c), end=' ')

if tot == 2:
    print('\n\033[mO número {} foi divisível apenas por 1 e por ele mesmo.'.format(num)) #Quebrei a linha e tirei a cor.
    print('Por isso, ele é um número PRIMO!')
else:
    print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
    print('Por isso ele NÃO É PRIMO!')
