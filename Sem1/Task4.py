#Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]

def get_n_numbers(num_n):
    if num_n <= 0:
        return []
    list_n = [1]
    product = 1
    for i in range(2, num_n + 1):
        product *= i
        list_n.append(product)
    return list_n


print(get_n_numbers(9))