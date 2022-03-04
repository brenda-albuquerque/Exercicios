'''Confira se a frase que você digitar é um palíndromo'''

frase = input("Digite uma frase: ").upper().strip()
if frase == frase[::-1]:
    print (f'{frase}')
    print("A frase é um palíndromo!")
else:
    print(f'{frase}')
    print("A frase não é um palíndromo")
