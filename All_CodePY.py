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
#что такое функция def?
# def - задает функцию (функции - Многократно используемые части кода )
alian = 10
balian = 'str_name'
def def_name():
    calian = (str(alian) + balian)
    print(calian)
print(def_name())
print("Finish function")
"""
"""
alian = 0
def increment():
    global alian
    #global - Возвращает словарь, представляющий текущую глобальную таблицу символов. Это всегда словарь текущего модуля
    # (внутри функции или метода, это модуль, где он определен, а не модуль, из которого она называется).
    alian = alian + 1
print(alian) #0
increment()
print(alian) #1
increment()
print(alian) #2
"""