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
"""
n = int(input("Факториал числа ") )
fac = 1
i = 0
while i < n:
     i += 1
     fac = fac * i
print ("равен",fac)
"""
#=========================================================DZ-L6==================================
"""
# THE MYSTICAL OCTOSPHERE!


import random
import time

print("Сияниче магического Шара сковало ваш взор...")
time.sleep(0.5)
questions = input(str("Задайте свой вопрос магическому Шару..." + "\n"))
time.sleep(0.5)

def number_to_fortune(num):
    if num == 0:
        return "Да, точно!"

    elif num == 1:
        return "Вероятно, да ..."

    elif num == 2:
        return "Кажется, да ..."

    elif num == 3:
        return "Определенно нет!"

    elif num == 4:
        return "Вероятно, нет"

    elif num == 5:
        return "Я действительно в этом сомневаюсь ..."

    elif num == 6:
        return "Не уверен, зайдите позже!"

    elif num == 7:
        return "Я действительно не могу сказать"

    else:
        return "Я обычный шар, а не предсказатель!"

num = random.randrange(0, 7)
time.sleep(0.5)

#print(number_to_fortune(num))
#TEST#print(number_to_fortune(17))
#time.sleep(3) # zaderzka ispolnenia v 3 sec
time.sleep(0.5)

print("И так, Ваш вопрос ... - " + str(questions))
time.sleep(1)

print("Ты трясешь мистический Шар ...")
time.sleep(0.8)

print("Магические завихрения приковывают твой взор ...")
time.sleep(0.6)

print("Магический Шар говорит ..." + str(questions) + "\n" + (number_to_fortune(num)))
"""