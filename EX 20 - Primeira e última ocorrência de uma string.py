# Entrada

frase = str(input('Digite uma frase: ')).lower().strip()

# Saída
print('Analisando frase...')
print('A letra A apareceu {} vezes nesta frase.'.format(frase.count('a')))
print('Aparecendo a primeira vez na posição {}'.format(frase.find('a') + 1))
print('e a última vez na posição {}.'.format(frase.rfind('a') + 1))
