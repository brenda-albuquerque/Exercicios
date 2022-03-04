''' Descubra se o seu número é um número primo.'''

x = int(input("Digite um número: "))
div = 0
for i in range(1, x + 1):
    if x % i == 0:
        print(f'\033[1;32m', end=' ')
        div += 1
    else:
        print('\033[1;31m', end=' ')
        primo = 'false'
    print(f'{i}', end='')

if div == 2:
    print(f" -> \033[4m{x}\033[m \033[32mé um número primo!")
else:
    print(f" -> \033[4;33m{x}\033[m\033[33m não é um número primo!")
