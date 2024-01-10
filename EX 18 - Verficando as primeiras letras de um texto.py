# Entrada

cidade = str(input('Qual a cidade? ')).strip()

# Saída

print(cidade[:5].upper() == 'SANTO')

'''A ideia no print é que o programa selecione até o elemento de
indexação 4 (suficiente pra ler Santo no primeiro nome) e transformá-lo
em todo maiúsculo para que o programa leia todas as variações que se
podem escrever Santo.'''
