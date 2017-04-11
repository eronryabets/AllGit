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

#Lessons 4
#==================================================================================

"""
def (x):
    print(x)

y = 52
f(y)
"""
"""
def f():
    a = 10
    s = "abc"
    return x+a


"""

"""
#1 Первый пример - Аргументы функции и возращаемые значения
y = 42


def f(x):
    print(id(x))
    x += 10
    print(x)
    print(id(x))


def g():
    print(y)


#def h():
    #y = 10
    #print(y)
#она создает переменную внутри себя, Y используется внутри функции, это локальная переменная
#он различин с внешним Игриком в переменной

def h():
    global y #глобал говорит что переменная Y должна взяться снаружи
    print(id(y))
    #тоже создал переменную игрик, и перезатер глобальный Y
    y += 10 # это меняет значение и с наружи, влияет на наружнюю переменную
    print(id(y))
    print(y)

print(id(y))
f(y)
print(id(y))
print(y)
g()
#Питон когда встречает незнакомое имя переменной ( область видимость) то он пытаеться искать эту переменную во всем коде
h() # внутри функции поменяла значение ИД Игрика, потом вышла (и изза глобала) тоже сменила значение Игрика
print(id(y))


#Передача аргументов по значению - когда нужно где то хранить данное значение, важно сохрн значение индификатора
"""
"""
#Пример 2

def f():
    print(42)


f()
# - это обычная функция
# max("abc") - обычная функция

s = "Abc"

s.lower()
#help(str) # необходимо прочитать хелп стринга

#def f (x):
#     ''.split()
# Программа получает данные в row (сырые данные - оригинале) формате ( не пригодны для потребления для самой программы)
# для этого используется метод strip()что бы вычитывать не нужные данные из файла, отсеить пробелы в начале и концу и тд
# isnumber() isalpha()
"""

"""
#Пример 3
x = -42

if x > 0:
    print("x is positive")
#elif x < 0:
#    print("x is negative")
"""


"""
#Пример 4


def abs_x(x):
    if x < 0:
        return -x

    #pass
    return x


#инкрементальная разработка и декомпозиция
x = 10
assert abs_x(x) == 10
#assert это тест
x = -2
assert abs_x(x) == 2
# assert проверяет условие, при Тру - тогда вернет значение.
# приучить себя - выполнять тесты, до момента реализации, написали функцию, написали тесты под нее
# след етап - пишем реализацию етой функции
# на экран ошибки не вывелись - тесты прошли успешно
# Следующий тип - это альтернативное выполнение
"""
"""
#Пример 5
x=5
if x %2 == 0:
    print("{} is even".format(x))
else:
    print("{} is odd".format(x))

"""

"""
#Пример 6 - Булево значение - либо тру либо фолс

def is_even(x):
    if x % 2 :# 0 - остатка нет, четное. А 1 - не четное . 1 - тру, 0 - фолс
        return False
    else:
        return True


x = 10
assert is_even(x) == True

x = 7
assert is_even(x) == False
"""

"""

#Пример 7

#Программа - Тесты - Документация
# if - elif (одно или несколько) - в конце else
x = 10
y = 1
if x < y:
    print("{} is less than {}".format (x, y))
#elif abbreviation else if
elif x > y:
    print("{} is greater than {}".format(x, y))
else :
    print("{} and {} are equal".format(x, y))

# switch - в питоне такого оператора нет, он в роли Иф и Елс

"""

"""

#Пример 8

def function_c():
    pass


choise = "D"

if choise == "A":
    function_a()
elif choise ==  "B":
    function_b()
elif choise == "C":
    function_c()
else:
    print("Invalid choise.")


print("Next line")

"""
"""
#x = 2
x = "a"
#print(len(x))
print(ord("a"))

if x < 97:
    print("x less than 2")
elif x  >= 97:
    print("x equal or greater 2")
else:
    print("Smth else")

#print(ord("a")) - по букве - возвращает его числовое значение (под каким оно идет)
# пайтон3 сравнивает еще типы конструкции и ето не проходит, во 2м проходит

"""

"""
#Пример 9

x = 9

if x < 2:
    print("{} less than 2".format(x))
elif x < 20:
    print("{} less than 20".format(x))
elif x < 10:
    print("{} less than 10".format(x)) #никогда не будет выполнен, статическая часть кода
else:
    print("Smth else")

"""

"""

#Exercise lecture 4

#hours = 42
#rate = 10
#2а аргумента
#hours <= 40
#hours * rate
#если 42а отработали, и рейт 10 уе в час - то должны посчитать 40 по 10 и 2а по 15
"""
"""
def calc_paid(hours, rate):
    paid = None
 if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else:
        paid = hours * rate
    return hours * rate
# нарушение модульности, один вход один выход, тут два выхода

assert calc_paid(20, 10) == 200
assert calc_paid(42, 10) == 430

"""

"""
#Перепишите расчет зарплаты, чтобы дать сотруднику
#1,5-кратная почасовая ставка для часов, отработанных свыше 40 часов.

#Время работы: 45
#Введите тариф: 10
#Оплатить: 475,0

hours = int(input("Введите рабочие часы: "))
rate = 10

def calc_paid(hours, rate):
    if hours > 40:
        return 40 * rate + ((hours - 40) * 15)
    else:
        hours <= 40
        return 40 * rate

pay = calc_paid(hours, rate)
print(pay)


assert calc_paid(40, 10) == 400
assert calc_paid (45, 10) == 475

"""
"""
#проверка четного чесла - оператор целочисленного деления, если число на 2 делиться - четное
#если осталась 1 - значит число не четное.
#print(10%2)#0

print("Проверка четности числа")
number = int(input("Введите ваше число "))
if number%2 == 0:
    print(number, " число четное")
else: print(number, " число не четное")
"""
"""
def atom(number):
    if number % 2 == 0:
        print(number, " число четное")
    else:
        print(number, " число не четное")


print(atom(int(input("введите число "))))
"""
"""
x = 2
y = 2
lol = int(x + y)
#print(type(lol))
#print(lol) #4

asder = lol
def increment():
    global asder
    asder = asder + 1

increment()
increment()
print(asder)

def treedef ():
    return asder + lol + 5



print(treedef())

"""

"""
print("Проверка четности числа")
number = int(input("Введите ваше число "))
if number%2 == 0:
    print(number, " число четное")
else: print(number, " число не четное")
"""
"""
def atom(number):
    if number % 2 == 0:
        print(number, " число четное")
    else:
        print(number, " число не четное")


print(atom(int(input("введите число "))))
"""
"""
number = int(input("input your numbers "))
if 0 <= number <= 13:
    print(number, "Ha ha ha")
else:
     number > 13
     print("ok")
if number > 15:
    print("No")


#print(10 < 20 < 30)

"""
"""
number = int(input("input your numbers "))
if 0 <= number <= 30:
    print(number, "first")
elif 31 <= number <= 60:
    print("second")
else:
    number > 61
    print("Third")
"""

"""

number = int(input("input your numbers "))
if 0 <= number <= 30:
    print(number, "first")
#elif  number >= 30 and number <= 60:
#    print("second")
elif 31 <= number <= 60:
    print("second")
else:
    number > 61
    print("Third")
"""
"""

x = 11
if 0 < x < 10:
    print("x is a positive single digit.")

"""

"""
x = 2

if x < 2:
    print("x less than 2")
elif x >= 2:
    print("x equal or greater 2")
else:
    print("Never print") #это условие никогда не выполниться
"""

"""
if x < 2:
    print(x, " less than 2")
elif x < 20:
    print(x, " less than 20")
elif x < 10:
    print(x, " less than 10") #это условие никогда не выполниться
else:
    print("Smth else")
"""
"""
number = float(input("Enter your numbers "))
print(number)

"""
"""
#МОЙ код
hours = int(input("Введите рабочие часы: "))
rate = 10

def calc_paid(hours, rate):
    if hours > 40:
        return 40 * rate + ((hours - 40) * 15)
    else:
        hours <= 40
        return 40 * rate

pay = calc_paid(hours, rate)
print(pay)


assert calc_paid(40, 10) == 400
assert calc_paid (45, 10) == 475
"""
"""
def current (x):
    return x += 1

print(current (5))
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
increment()
print(alian) #2

"""
"""
def lol(x, y):
    return x + y

lol(2,2)
print(lol(2,2)) #4

asder = float(lol)

def increment():
    global asder
    asder = asder + 1

increment()
print(increment())


"""
"""
x = 2
y = 2
lol = int(x + y)
#print(type(lol))
#print(lol) #4

asder = lol
def increment():
    global asder
    asder = asder + 1

increment()
increment()
print(asder)

def treedef ():
    return asder + lol + 5



print(treedef())

"""
"""
#ПОВТОРЕНИЕ
print("test chetnogo chisla")
numbers = float(input("enter your number "))
if numbers % 2 == 0 :
    print("Chetnoe")
else:
    print("ne chetnoe")

"""
"""
#ПОВТОРЕНИЕ
# Перепишите расчет зарплаты, чтобы дать сотруднику
# 1,5-кратная почасовая ставка для часов, отработанных свыше 40 часов.
# время работы 45 часов \ 40 ч = по 10 \ дальше по 15

hours = float(input("Введите часы вышей работы "))
rate = 10


def calc_paid(hours, rate):
    if hours >= 41:
        return 40 * rate + ((hours - 40) * 15)
    else :
        return hours * 10

print(calc_paid(hours, rate))

#assert calc_paid(40, 10) == 400
#assert calc_paid(42, 10) == 430
"""
"""
#ПОВТОРЕНИЕ
#14 i 51
time = int(input("Введите время "))
current_timer = int(input("Введите время таймера "))
x = (current_timer % 24) + time
print("Таймер сработает, когда будет " ,x)
"""
"""
#ПОВТОРЕНИЕ
# 0 - 30 - first\ 31 -60 second\ 61 - 100 third

years = int(input("Введите возраст "))
if years <= 30:
    print("first")
elif 31 <= years <= 60:
    print("second")
else:
    years >= 61
    print("third")

"""


