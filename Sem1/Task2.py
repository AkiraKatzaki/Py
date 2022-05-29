#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def count_occurrences(str1, str2):
    count = 0
    for i in range(len(str1) - len(str2) + 1):
        flag = True
        for j in range(len(str2)):
            if str1[i+j] != str2[j]:
                flag = False
                break
        if flag:
            count += 1
    return count


print(count_occurrences("", ""))  # Пользователь вводит данные
