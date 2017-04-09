

#increment = прирост
alian = 0
def increment():
    global alian
    #global - Возвращает словарь, представляющий текущую глобальную таблицу символов. Это всегда словарь текущего модуля
    # (внутри функции или метода, это модуль, где он определен, а не модуль, из которого она называется).
    #Вообщем global запоминает последнее значение нашей переменной "alian" и при каждом вызове добавляет + 1
    alian = alian + 1
print(alian) #0
increment()

balian = 2

def increment2():
    global balian
    alian = balian + 1

lora = increment + increment2
print(lora)
