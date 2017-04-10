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
def dirname():
    import os
    print("Файлы и папки дирректории : ", os.listdir('.'))
    return os.listdir('.')

print(dirname())
"""

"""
def f():
    x = 42
    #return x
print(f())

Функция в оприоре должна что то вернуть, если ретурн не задан она вернет None

"""

