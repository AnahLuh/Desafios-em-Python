
print('GERADOR DE PA')
print('-='*8)

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

c = primeirotermo
while c < primeirotermo + (10 - 1) * razao + razao:
    print(c, end = ' → ')
    c = c + razao
print('FIM')