from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))

idade = atual - ano # Idade do Homem

if idade > 18:
    print('Você tem {} anos e deveria ter se alistado em {}.'.format(idade, atual - (idade - 18)))
elif idade == 18:
    print('Você já tem 18 anos. Está na hora de você se alistar!')
else:
    print('Você tem {} anos e só deve se alistar em {}.'.format(idade, atual + (18 - idade)))