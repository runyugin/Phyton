# Задача 1


n = int(input())

fact = 1

if n == 0:
    print(fact)
else :
    while n>1:
        fact *= n
        n -= 1
    print(fact)


