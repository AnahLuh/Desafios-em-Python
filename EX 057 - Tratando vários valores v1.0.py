num = s = 0
c = 0
while num != 999:
    num = int(input('Digite um número[999 para parar]: '))
    if num == 999:
        break
    s += num
    c = c + 1

print('A soma destes {} valores é de {}.'.format(c, s))
