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





























































