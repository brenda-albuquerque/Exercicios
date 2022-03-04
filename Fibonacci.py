'''O programa lê um número n e retorna a quantidade de termos Fibonacci solicitados.'''

n = int(input("Digite quantos termos você gostaria: "))
x1 = 0
x2 = 1
i = 3
print(f"{x1}-{x2}", end='')
while i <= n:
    x3 = x1 + x2
    print(f"-{x3}", end='')
    x1 = x2
    x2 = x3
    i += 1
