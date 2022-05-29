# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def product_num(list_n):
    i = 0
    result_list = []
    while 2 * i <= len(list_n) - 1:
        result_list.append(list_n[i] * list_n[len(list_n) - 1 - i])
        i += 1
    return result_list


print(product_num([2, 3, 4, 5, 6]))
print(product_num([2, 3, 5, 6]))
