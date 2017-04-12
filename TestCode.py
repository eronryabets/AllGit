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
#"""
def print_line(n):
    counter = n

    while counter > 0:
        print()
        counter -= 1
        #n = n - 1
print_line(4)
