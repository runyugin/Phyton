# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


n = int(input())

import random

arr = []

k = 1

for i in range(n):
    arr.insert(i, random.randrange(0,100))

print(*arr)

x=arr[n//2]
x_count =  arr.count(x)


print('X = ', x, ', встречается ', x_count, ' раз')