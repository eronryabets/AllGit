#LECTURE #

"""
prefix = 'Привет, '
name = input('Введите свое имя: ')
name_prb = name + ' '
fam = input('Введите свою Фамилию: ')
print('{} :) {}{}'.format(prefix, name_prb , fam+'!'))  #Привет,  :) Asder Aderovich!
"""
"""
#14 i 51
current = input("vvedite vase vremya ")
timer_hours = input("vvedite chasov timera ")
timer_off = ((int(current) + int(timer_hours)) % 24)
print("Timer viklychitsa kogda na chasah bydet ", timer_off)
"""
"""
alian = print(type(32))
alian
balian = type(32)
print(balian)
"""
"""
#сейчас 14 часа ставим таймер на 51, во сколько времени он сработает
time = 14
hours = 51
time_timer = (hours + time) % 24
print(time_timer ) #17
"""
"""
print(id(3))
alian = 3
print(id(alian))
"""
"""
print(float(99/100))
a = 50.0 #class float
b = 50 #class int
print(type(a))
print(type(b))
print(a + b)
c = a + b
print(type(c))
print('word.............................')
print(str(555) + "word") # = print(format(555) + "word")
#format(555) = str(555) Форматирование (обычно форматирование строки).
"""

"""
a = 50
print(type(a)) #int
f = float(a)
print(f) #float 50.0
print(type(f)) #float
print(1 + 2 * float(3) / 4 - 5 - 2.5) #  =  (1 + (2 * float(3) / 4) - 5 - 2.5) = 1 + (1.5) - 5 - 2.5  = -5.0
"""

"""
#Python также может преобразовывать числа с плавающей точкой в целые числа
#(помните, что число обрезается до целой части):
print(int(3.9999999)) # int = 3
print(int(-2.3)) # int = -2
"""

"""
#Конвертация типов
#float преобразуем в число с плав.точкой
print(float(50))
print(float('3.14'))
#str преобразуем в строчку
print(str(50))
print(str(3.14))
"""

"""
alian = "123"
print(type(alian)) #str
#print(alian + 1) #error
balian = int(alian)
print(type(balian)) #int
print(balian + 1 ) # = 124 преобразовали значение в Инт и выполнили сложение 123 + 1
#calian = "hello"
#dalian = int(calian) ValueError: invalid literal for int() with base 10: 'hello'
"""
"""
#приведение типов ( можем решить проблему целоисленного деления)
minute = 59
print(float(minute/60)) # прошла 0.9833333333333333 ая часть часа
#другой вариант ввести плав.точку
minute = 59
print(minute/60.0)
#Пример неявного преобразования типа
"""
"""
#Математические функции
import math
print(3.14 / 2)
pi = 3.14
x = 10.0
print(1/x)
print(math.sin(pi/2)) #0.9999996829318346
print(math.log(1/x)) #-2.3025850929940455
print(math.log(1/math.sin(pi/2))) #3.170682155987296e-07
"""
"""
#Математические функции
import math
decibel = math.log10 (17.0) # log base 10; log base e
angle = 1.5
height = math.sin(angle) # radian
"""
"""
#Композиция

"""
"""
#increment = прирост
#global - Возвращает словарь, представляющий текущую глобальную таблицу символов. Это всегда словарь текущего модуля
# (внутри функции или метода, это модуль, где он определен, а не модуль, из которого она называется).
#Вообщем global запоминает последнее значение нашей переменной "alian" и при каждом вызове добавляет + 1

alian = 0
def increment():
    global alian
    alian = alian + 1

increment()
increment()
print(alian) #2

balian = 2

def increment2():
    global balian
    balian = balian + 1

increment2()
increment2()
print(balian) #4

print(alian + balian) #6
"""

"""
def add(x, y):
    return x + y

print(add(1, 20))
"""

"""Анонимные функции, инструкция lambda
Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее. Анонимные функции
 создаются с помощью инструкции lambda. Кроме этого, их не обязательно присваивать переменной,
 как делали мы инструкцией def func():

 lambda функции, в отличие от обычной, не требуется инструкция return, а в остальном, ведет себя точно так же:

func = lambda x, y: x + y
print(func(1,4))
"""
"""
#=============================================================================================
​i = 3
j = 3
print  id(i)
print  id(j)
j = j + 1
print hex(id(j))


hex преобразует целое число в строчную шестнадцатеричную строку с префиксом «0x»

a = 5
b = 5.0

print(5, 5.0)
print("id:", "\na:", id(a), "\nb:", id(b))
print("hex", "\na:", hex(a), "\nb:", float.hex(b))
print(int(0x5)) #преобразования шестнадцатеричной строки в целое число
=====================
a = 5
print(a) #a
print(id(a)) #501392608
print(hex(a)) #0x5
print(hex(id(a))) #0x1de2a4e0
print(int(0x5)) #5
print(int(0x1de2a4e0)) #501392608 если заИнтить Хексовое значение, то вернеться ИД

#как узнать по ID какому именно обьекту он пренадлежит?
#=============================================================================================
"""
"""
count = 0

def increment():
    global count
    count = 10
    count = count + 1
    print(hex(id(count)))

print(count)
increment()
print(count)
print(hex(id(count)))

#0
#0x1e04a5a0
#11
#0x1e04a5a0
"""
#====================================================================================================
"""
#Пример наличия доступа файла фуу тхт
#https://www.tutorialspoint.com/python/os_access.htm
#http://www.ilnurgi1.ru/docs/python/modules/os.html?highlight=os.name#os.name
import os, sys

ret = os.access("C:/Games/foo.txt", os.F_OK)
print("F_OK - return value %s"% ret)

"""
"""

import os
print("OS name: ", os.name)
print("Файлы и папки дирректории : ", os.listdir('.')) #список всех файлов и дирректорий в корне где и данный скрипт
#ret = (os.access("C:/Git/AllGit/", os.F_OK))
#print("F_OK - return value %s"% ret)
print("Наличие правильности пути: ", os.access("C:/Git/AllGit/", os.F_OK))
#print(os.listdir("C:/Games/")) # выводит список файлов и папок указанной директории
#diros = input("Введите свою дирректорию : ")
#print(os.listdir("C:/Games/"))
print("Введите дирректорию, файлы которой хотите просмотреть: ")
print("В данной директории : ", os.listdir(input()))
"""
"""
#1
import os
print("Файлы и папки дирректории : ", os.listdir('.')) #список всех файлов и дирректорий в корне где и данный скрипт
"""
"""
# Задача 2: Напишите функцию, принимающую в качестве аргумента директорию,
# и печатающей список всех файлов в данной директории.



def dirname():
    import os
    print("Файлы и папки дирректории : ", os.listdir('.'))
    x = os.listdir('.')
    return os.listdir('.')

print(dirname())
"""

"""
#v2
def dirname():
    import os
    print("Введите дирректорию, файлы которой хотите просмотреть: ")
    print("В данной директории : ", os.listdir(input()))
    return os.listdir('.')

print(dirname())
"""
#==================================================================================


"""
def printTwice(bruce):
  print(bruce, bruce)
 printTwice(bruce)
"""
"""
def add(x, y):
    return x + y

print(add(1, 20))
"""

"""Анонимные функции, инструкция lambda
Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее. Анонимные функции
 создаются с помощью инструкции lambda. Кроме этого, их не обязательно присваивать переменной,
 как делали мы инструкцией def func():

 lambda функции, в отличие от обычной, не требуется инструкция return, а в остальном, ведет себя точно так же:

func = lambda x, y: x + y
print(func(1,4))
"""
"""
def catTwice(part1, part2):
    cat = "part1" + "part2"

catTwice("aaa", "bbb")
print(cat)
"""
# Задача 1: Напишите функцию, печатающую список всех файлов в текущей директории.

# Задача 2: Напишите функцию, принимающую в качестве аргумента директорию,
# и печатающей список всех файлов в данной директории.

# Задача 3: Перепишите предыдущую функцию таким образом,
# чтобы в случае задания аргумента она печатала содержимое указанной директории,
# и печатающей список всех файлов в данной директории если директория не указана.

"""
#Пример наличия доступа файла фуу тхт
#https://www.tutorialspoint.com/python/os_access.htm
#http://www.ilnurgi1.ru/docs/python/modules/os.html?highlight=os.name#os.name
import os, sys

ret = os.access("C:/Games/foo.txt", os.F_OK)
print("F_OK - return value %s"% ret)

"""
"""

import os
print("OS name: ", os.name)
print("Файлы и папки дирректории : ", os.listdir('.')) #список всех файлов и дирректорий в корне где и данный скрипт
#ret = (os.access("C:/Git/AllGit/", os.F_OK))
#print("F_OK - return value %s"% ret)
print("Наличие правильности пути: ", os.access("C:/Git/AllGit/", os.F_OK))
#print(os.listdir("C:/Games/")) # выводит список файлов и папок указанной директории
#diros = input("Введите свою дирректорию : ")
#print(os.listdir("C:/Games/"))
print("Введите дирректорию, файлы которой хотите просмотреть: ")
print("В данной директории : ", os.listdir(input()))
"""
"""
#1
import os
print("Файлы и папки дирректории : ", os.listdir('.')) #список всех файлов и дирректорий в корне где и данный скрипт
"""
"""
# Задача 2: Напишите функцию, принимающую в качестве аргумента директорию,
# и печатающей список всех файлов в данной директории.



def dirname():
    import os
    print("Файлы и папки дирректории : ", os.listdir('.'))
    return os.listdir('.')

print(dirname())
"""
"""

def dirname():
    import os
    print("Введите дирректорию, файлы которой хотите просмотреть: ")
    print("В данной директории : ", os.listdir(input()))
    return os.listdir('.')

print(dirname())
"""
# Задача 3: Перепишите предыдущую функцию таким образом,
# чтобы в случае задания аргумента она печатала содержимое указанной директории,
# и печатающей список всех файлов в данной директории если директория не указана.
"""
def dirname():
    import os
    print("Введите дирректорию, файлы которой хотите просмотреть: ")
    print("В данной директории : ", os.listdir(input()))
    return os.listdir('.')

print(dirname())
"""