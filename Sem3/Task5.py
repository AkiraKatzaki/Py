# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

def rec(number): # запись в файл
    data = open('text.txt', 'w')
    data.write('\n'.join(number))
    data.close()
    return number

def read():
    path = 'text.txt'
    data = open(path, 'r')
    lst = []
    for i in data:
        if int(i.strip('\n')) % 2 == 1:
            lst.append(i.strip('\n'))
    print(lst)
    data.close()
    return lst

print(rec(['235', '232', '233', '264', '345', '624', '342', '123', '516', '127'])) # запись в файл
rec(read())  # перезапись