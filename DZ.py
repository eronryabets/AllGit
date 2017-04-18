# -*- coding: utf-8 -*-
"""
#Пример решению при помощью Range

Напишите программу, которая печатает сумму чисел от 1 до 101 (включены 1 и 101)
Которые делятся на 5 (используйте цикл while)
Ответ: 1050

aggregate = 0 # в эту перменную сумируем числа
numbers = range(0, 101)
for i in numbers:
    #print(i)
    if i % 5 == 0:
        aggregate += i

print(aggregate)
assert aggregate == 1050


"""
"""
#Пример решению при помощью Range

#Напишите программу, используя цикл while,
#который печатает сумму каждого третьего числа от 1 до 1001 (включены 1 и 1001)
#(1 + 4 + 7 + 10 + ....)
#Ответ: 167167


aggregate = 0
numbers = range(1, 1001, 3)
for i in numbers:
    print(i)
    aggregate += i


print(aggregate)
"""

"""
#While Loop, Упражнение 2
#Напишите программу, используя цикл while, который попросит пользователя ввести положительное целое число, n,
#И затем печатает факториал n.
#Факториал определяется как произведение всех чисел от 1 до n (1 и n включительно)
#Например, когда пользователь вводит: 5
#Ваш распечатанный результат:
#120


#import math
#n = int(input("Введите целое число..."))
#print("Факториал вашего целого числа ", math.factorial(n))

n = int(input("Введите положительное целое число: "))
def fac(n):
    fac = 1
    i = 0
    while i < n:
        i += 1
        fac = fac * i
    return fac
print("Факториал вашего числа: ",fac(n))


"""