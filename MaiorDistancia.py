'''Em um campeonato de arremesso de dardo, o atleta tem 3 chances.
O objetivo é lançar o dardo à maior distância que conseguir.
O programa a seguir informará qual foi a maior distância'''

print ('Informe as três distâncias:')
a = float(input('01: '))
b = float(input('02: '))
c = float(input('03: '))
print(' ')

if a > b and a > c:
    print(f"A maior distâcia foi {a}")

elif b > a and b > c:
    print(f"A maior distâcia foi {b}")

else:
    print(f"A maior distâcia foi {c}")
