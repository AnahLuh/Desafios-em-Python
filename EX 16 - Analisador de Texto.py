nome = str(input('Qual o seu nome completo? ')).strip() # Desconsidera os espaços antes e depois da string

print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {}.'.format(len(nome) - nome.count(' '))) # Conta as letras removendo os espaços entre as palavras

