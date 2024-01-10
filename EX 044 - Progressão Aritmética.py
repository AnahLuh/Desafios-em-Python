termo = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))

for cont in range(termo, (termo + (10 - 1)) * razao + razao, razao): # 10 porque são os 10 primeiros termos.
    print(' {} '.format(cont), end= '→') # Pra fazer a setinha é "Alt + 26"
print(' FIM ')