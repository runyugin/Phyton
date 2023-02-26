# Задача 1

import math

n = 700
m = 850

days = m/n

print(math.ceil(days))

# Задача 2

class_1 = 20
class_2 = 21
class_3 = 22

table = (class_1//2 + class_1%2) + (class_2//2 + class_2%2) + (class_3//2 + class_3%2)

print(table)

# Задача 3

# i = int(input())
# j = int(input())

# if i == j:
#     print('нужна доп информация')
# else:
#     print(i+j-1)


# Задача 4

i = int(input())

if i%400==0:
    print('YES')
elif i%4==0 and i%100!=0:
    print('YES')
else:
    print('NO')