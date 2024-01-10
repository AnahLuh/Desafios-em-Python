infos = {}

infos['nome'] = str(input('Digite o nome do aluno: '))
infos['media'] = float(input('Digite a sua média: '))

if infos['media'] < 6:
    infos['situação'] = 'REPROVADO'
elif infos['media'] > 6:
    infos['situação'] = 'APROVADO'

print(f'O aluno {infos["nome"]} teve média igual a {infos["media"]}.')
print(f'Portanto, foi {infos["situação"]}.')