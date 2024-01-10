sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] # Só pega a primeira letra

while not sexo in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')