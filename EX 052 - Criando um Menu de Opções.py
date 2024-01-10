n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

op = 0

while op != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    op = int(input('>>>>>>>> Qual a sua opção? '))
    if op == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}.')
    elif op == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
    elif op == 3:
        if n1 < n2:
            print(f'O maior número é {n2}.')
        if n2 < n1:
            print(f'O maior número é {n1}.')
    elif op == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')

print('Fim do programa. Volte sempre!')


