#Сформировать список из N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

def get_n_numbers(num_n):
    if num_n <= 0:
        return []
    list_n = [1]
    product = 1
    for i in range(num_n - 1):
        product *= -3
        list_n.append(product)
    return list_n


print(get_n_numbers(0))
