# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def get_n_numbers(list_n):
    sum = 0
    for i in range(len(list_n)):
        if i % 2 == 0:
            sum += list_n[i]
    return sum


print(get_n_numbers([34, 2, 6, 4]))
