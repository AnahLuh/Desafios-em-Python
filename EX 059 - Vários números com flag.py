num = 0
soma = 0
n = 0

while True: # Loop infinito
    num = int(input('Digite um valor [Digite 999 para parar]: '))

    if num == 999:
        break

    soma += num
    n += 1

print(f'A soma destes {n} valores foi {soma}!')

