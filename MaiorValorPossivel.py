'Maior valor possível de uma lista.'

numbers = [-3, 0, 15, 2, 7, 13, 5, 17, 9]

max_value = 0

for num in numbers:
    if (max_value <= 0):
        max_value = 1

    elif (num > max_value):
        max_value = num - 1

print('Maximum value:', max_value)
