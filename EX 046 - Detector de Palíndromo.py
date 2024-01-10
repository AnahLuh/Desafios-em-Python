frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[:: -1] # Lê toda a frase de trás pra frente.

'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

print('O inverso da frase {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('Não temos um palíndromo.')