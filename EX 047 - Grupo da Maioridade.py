from datetime import date
atual = date.today().year
maiores = 0
menores = 0

for c in range(1, 8):
    data = int(input('Data de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - data
    if 18 <= idade:
        maiores += 1
    else:
        menores += 1

print('Dentre estas 7 pessoas, há {} pessoas maiores de idade e {} pessoas menores de idade.'.format(maiores, menores))
