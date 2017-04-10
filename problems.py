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

"""
hours = 42
rate = 10

def calc_paid(hours, rate):
    #paid = None
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else:
        #paid = hours * rate
        return hours * rate
# нарушение модульности, один вход один выход, тут два выхода

pay = calc_paid(hours, rate)
print(pay)
assert calc_paid(20, 10) == 200
assert calc_paid(42, 10) == 430
# ЗАЧЕМ нужна переменная paid - когда код выполняеться и без нее?
#================================================================
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
# проблема была, что при вводе 63, выводило и второй и третий, но тогда я не использовал elif
# ввод 61, не исполняется при if и elif, следовательно использовался и завершился при else

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
