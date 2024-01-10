# ...

print('='*25)
x = 'BANCO'
print('{:^25}'.format(x))
print('='*25)

# cinquenta = total // 50
# vinte = (total - (cinquenta * 50)) // 20
# dez = (total - (cinquenta * 50 + vinte * 20)) // 10
# um = (total - (cinquenta * 50 + vinte * 20 + dez * 10)) // 1

valor = int(input('Quantos reais você quer sacar? R$ '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break




