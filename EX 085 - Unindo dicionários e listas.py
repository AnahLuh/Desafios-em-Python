pessoa = {}
somaidade = 0
listaprinc = []
listamulher = []
maior_media = []
q = 0

while True:
    q += 1 # Pra personalizar o input

    print('-='*15)
    print(f'{q}º PESSOA')

    pessoa['nome'] = str(input(f'Nome: ')).rstrip().lstrip()
    pessoa['sexo'] = str(input('Sexo: ')).strip()[0].upper()
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Digite o sexo novamente!')
        pessoa['sexo'] = str(input('Sexo: ')).strip()[0].upper()
    if pessoa['sexo'] in 'F':
        listamulher.append(pessoa['nome'])

    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']

    listaprinc.append(pessoa.copy()) # Tem que fazer uma cópia do dicionário para que os dois não se interliguem diretamente.

    opcao = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
    while opcao not in 'SN':
        print('ERRO!')
        opcao = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
    if opcao in 'N':
        break

    pessoa.clear()

media = somaidade / q

print()
print('-='*20)
print()

if q == 1:
    print('Foi cadastrada UMA pessoa.')
else:
    print(f'Foram cadastradas {q} pessoas.')

print(f'A média de idade das pessoas cadastradas é {media:.2f}.')

print(f'As mulheres cadastradas foram: ')
for c in listamulher:
    print(c)

for p in listaprinc:
    if p['idade'] >= media:
        print()
        for k, v in p.items():
            print(f'{k} = {v}; ', end= '')
        print()



