


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

big = max("Hello word")
print(big)


















































