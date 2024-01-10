from random import randint
from operator import itemgetter
dados = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}

print('Valores sorteados:')
for k, v in dados.items():
    print(f'{k} tirou {v}.')

ranking = sorted(dados.items(), key=itemgetter(1), reverse =True)

print()
print('-='* 20)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')