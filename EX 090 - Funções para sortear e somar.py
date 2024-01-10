from random import randint
num = []


def sorteia():
    for contador in range(0, 5):
        num.append(randint(0, 100))
    print(num)


def somapar():
    soma = 0
    for i in num:
        if i % 2 == 0:
            soma += i
    print(soma)


sorteia()
somapar()