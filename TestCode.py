


"""
#12. Повышенной сложности: Напишите Python функцию print_digits, которая принимает в качестве аргумента целое число
диапазоне [0,100), то есть наименьшее значение 0, но меньше чем 100. и печатает сообщение "The tens digit is %, and
 the ones digit is %.", где знак процента должен быть заменен соответствующими значениями. (Подсказка: используйте
 арифметические операторы целочисленного деления // и остатка от деления % для нахождения чисел.
"""
"""
import random
randnumber = random.randint(0, 100)
print(randnumber)
"""

"""
#ЛЕКЦИЯ 5 - параметры
def says(word):
    if word == "es":
        print("Ok - its ES")
    elif word == "fr":
        print("OK - its FR")
    else :
        print("No")


print(says("fr"))
"""
"""
def greet():
    return "Hello"
print(greet(), "Eron")
"""
"""
#ЛЕКЦИЯ 5 - возвращаемое значение
def says(word):
    if word == "es":
        return "Hello"
    elif word == "fr":
        return "Privet"
    else :
        return "Hi"

print(says("es"), "Eron")
"""
"""
big = max("Hello word")
print(big)
"""

"""
def addtwo (a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)
"""
"""
import math
def area(radius):
    temp = math.pi * radius**2
    return temp

print(area(180))
"""
"""
import math
def area(radius):
    return math.pi * radius**2
print(area(180))

"""
"""
#нахождение растояния между двумя точками - написал сам, дальше пример лекции - ниже под задачей
import math
def distance (x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2+(y2 - y1)**2)
print(distance (1,2,4,6))
#vernet 5.0 (verno)
"""
"""
#1 часть
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print("dx is ", dx)
    print("dy is ", dy)
    return 0.0
print(distance (1,2,4,6))
"""
"""
#часть 2
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    print("dsquared is: ", dsquared)
    return 0.0
print(distance (1,2,4,6)) #vivod 25
"""
"""
#часть 3
import math
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result
print(distance (1,2,4,6)) # 5.0
"""
"""
#Логические функции

def isDivisible(x, y):
  if x % y == 0:
    return True
  else:
    return False

print(isDivisible(1,4))

"""
"""
def isDivisible(x, y):
  return x % y == 0
print(isDivisible(1,4))
"""






































