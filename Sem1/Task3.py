#Подсчитать сумму цифр в вещественном числе.

def count_digit(number):
    count = 0
    str_num = str(number)
    for i in range(len(str_num)):
        if str_num[i] != '.':
            count += int(str_num[i])
    return count


print(count_digit(111.22))  # Пользователь вводит данные