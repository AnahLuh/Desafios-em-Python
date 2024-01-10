from random import randint
print('VAMOS JOGAR?')
print('''Escolha uma opção:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('O computador escolheu {}.'.format(itens[computador])) #Incorpora o intervalo [0, 2] na variável itens

if jogador == 1 and computador == 0:
    print('Vocês empataram o jogo!')
elif jogador == 1 and computador == 1:
    print('HAHAHA, o computador ganhou!')
elif jogador == 1 and computador == 2:
    print('PARABÉNS! Você venceu!')
elif jogador == 2 and computador == 0:
    print('PARABÉNS! Você venceu!')
elif jogador == 2 and computador == 1:
    print('Vocês empataram o jogo!')
elif jogador == 2 and computador == 2:
    print('HAHAHA, o computador ganhou!')
elif jogador == 3 and computador == 0:
    print('HAHAHA, o computador ganhou!')
elif jogador == 3 and computador == 1:
    print('PARABÉNS! Você venceu!')
elif jogador == 3 and computador == 2:
    print('Vocês empataram o jogo!')
else:
    print('Opção inválida! Tente novamente.')