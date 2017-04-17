"""
x = 42

if x == 42:
    print("Magic")

else:
    #TODO: add code later
    pass

print("next")

#Заглушка, на дальнейшую разработку.
"""
"""

x = "3"
if x <= 2:
    print("less ot equel")

else:
    print("Greater")
"""
"""
#в рекурсивной функции обязательно должно стоять условие

def countdown(n):
    if n == 0:
        print("Start")
        return

    print(n)

    countdown(n - 1)



countdown(10)
"""

"""
#n! = n*(n-1)!

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

assert factorial(3) == 6
print(factorial(5))
# 5 * 4 * 3 * 2 * 1 - факториал, тобишь вывод 120 верны№

"""

"""

#n! = n*(n-1)!
#Числа Фибоначи

def fibonacci(n):
    if n <= 0:
        return 1# c 0 не работал) что бы не нарушить сумму - при суммировании + 0 делаем. а при умножении умножаем на 1


    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(3) == 5

"""
"""
#While - LOOP - lecture 6
#вариант рекурсией выводим сто строк для печати
def print_line(n):
    if n == 0:
        return

    print()

    print_line(n-1)

print_line(100)
"""

#"""
# While - выполн ципочечные операции, работает со счетчиками
"""
def print_line(n):
    while n > 0:
        print("text")
        n -= 1



print_line(3)
"""
"""
def print_line(n):
    counter = n

    while counter > 0:
        print()
        counter -= 1
        #n = n - 1
print_line(4)

"""
"""
def print_line(n):
    if n <= 0:# до вайла - участок кода - наз гуардиан
        return #просто выходим из функции, если мотриц значение

    if not isinstance(n, int): # если N не исинстант - выйдем вообще
        return
    counter = n

    while counter > 0:
        print()
        counter -= 1
        #n = n - 1
"""

"""
print_line(4)
print_line(3.3)

def print_line(n):
    if (n <=0) or (not isinstance(n, int)):
        return

    counter = n

    while counter > 0:
        print()
        counter -= 1
        #n = n - 1


print_line(4)
print_line(3.3)
"""

"""

abc = "abc"
#ch - имя переменной к которой идет обращение в функции
if __name__ == '__main__':
    for ch in abc:
        print(ch)


#итерратор - заходит 4е раза, на 4ый раз видит маркер - что сымволы закончились и выходит

"""
"""
abc = "abc"
print(type(abc))

for ch in abc:
    print(ch, type(ch))

print(ch)
"""

"""

#нумерация в массивах идет с нуля


abc = "abcd"
i = 0
print(len(abc))

while i < len(abc):
    print("{}: {}".format(i, abc[i]))
    i +=1

#индекс полседнего символа -1
abc[len(abc)-1]

#while i < 3:
#    print(abc[i])
#    i += 1
#
#print(i)
"""

"""
abc = "abc"
#range возвращает цифры в заданом диапазоне 4 = 1 2 3
for i in range(len(abc)):
    print(abc[1])

"""

"""

#range(n) возвращает от 0 ... до n-1

#list(range(1,4,2))

s = "abcdefg"

for i in range(1, len(s), 2):
    print(s[i])

"""

"""
lecture6

    aggregate = 0 # в эту перменную сумируем числа

    for i in range(1, 102):
        aggregate += i

    print(aggregate)
"""
"""
#%timeit sum(range(1, 102))
print(10+1)
NEW LECTIONS 6
"""
"""
def f(x):
    return x ** 2

f(2)

def main():
    print(f(2))
if __name__ == "__main__": #eto blok yslovnogo vipolnenia
    main()

"""
"""
import time
print("one")
time.sleep(3) # zaderzka ispolnenia v 3 sec

print("two")


"""
"""

s = "生年月日"
us = u"生年月日"

# 1. Length
length = len(s)
print(length)

# 2. Last symbol
last = s[length-1]
print(last)

# 2. Last symbol
last = s[-1]
print(last)
"""

"""
def sequence(n):
    while n != 1:
        print(n, end='')
        if n % 2 == 0:  # n is even
            n = n / 2
        else:  # n is odd
            n = n * 3 + 1

sequence(5)
"""
"""
def get_temp():
    print("temperature")


def get_pressure():
    print("pressure")


while True:
    choise = input("Enter choise (1-temp, -pressure, q-quit: ")
    if choise == "1":
        get_temp()
    elif choise == "2":
        get_pressure()
    elif choise == "q":
        break
    else:
        print("Enter valid choise.")
"""
"""

while True:
    line = input()
    if __name__ == '__main__':
        if line[0] == "#": #esli pervi simvol reshetka to ..
            continue
        else:
            print(line)

"""
"""
s = "abc"

#s[len(s)-1]
s[-2]
"""

s = "abba"
#print(s[0] = "d" # "abba")
#"d" + s[1:len(s)] #libo tak - posled stroky. esli granica ne ykazana to on s nachala do konca
s = "abbaa"
"d" + s[1:4:2] #s 1go po 4iy s shagom 2 . shag mona i v otricatelnom vvesti :-1
#"d" + s