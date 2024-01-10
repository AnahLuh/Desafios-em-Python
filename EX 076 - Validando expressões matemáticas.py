a = 0 # Parenteses abertos
f = 0 # Parenteses fechados

expr = str(input('Digite a expressão: ')).strip()

for simb in expr:
    if simb == '(':
        a += 1
    if simb == ')':
        f += 1

if a == f:
    print('A expressão é válida!')
    print(f'Foram abertos e fechados {a} e {f} parênteses respectivamente.')
else:
    print('A expressão é inválida!')
    print(f'Foram abertos e fechados {a} e {f} parênteses respectivamente.')








