# Написать программу преобразования десятичного числа в двоичное

def convert(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(b)


print(convert(8))
