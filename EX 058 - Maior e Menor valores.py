opcao = 'S'
soma = qnt = media = 0
while opcao in 'Ss':
    num = int(input('Digite um valor: '))
    soma +=num
    qnt += 1

    if qnt == 1:
        menor = maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

    opcao = str(input('Quer continuar [s/n]?')).strip()[0].upper()

media = soma / qnt
print(f'Você digitou {qnt} números e a média foi de {media}.')
print(f'O menor e o maior valor foram, respectivamente, {menor} e {maior}.')


