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
# для этого используется метод strip() - что бы вычитывать не нужные данные из файла, отсеить пробелы в начале и концу и тд
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

#"""

#Exercise lecture 4

#hours = 42
#rate = 10
#2а аргумента
#hours <= 40
#hours * rate
#если 42а отработали, и рейт 10 уе в час - то должны посчитать 40 по 10 и 2а по 15

def calc_paid(hours, rate):
    if hours >= 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    return hours * rate


assert calc_paid(20, 10) == 200
assert calc_paid(42, 10) == 430

