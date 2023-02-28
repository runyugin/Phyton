# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


# n = int(input())

n = 9

arr = []

for i in range(n):
    arr.insert(i, i+1)

print(*arr)

x=arr[n//2]

print(x)

result = arr[0]

for i in range(len(arr)):
    if result<arr[i] and arr[i]<x:
        result=arr[i]

print('->', result)