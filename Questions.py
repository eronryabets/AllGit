#Вопросы
def printTwice(bruce):
  print(bruce, bruce)
 printTwice(bruce)

 что это за (bruce) ? в верху функции
#================================
def catTwice(part1, part2):
  cat = part1 + part2
  printTwice(cat)

#========================

def add(x, y):
    return x + y

print(add(1, 20))

#=============================

def func(*args):
    return args

#Функция также может принимать переменное количество позиционных аргументов, тогда перед именем ставится *:
# Не поенял, что делает *args

#==========================

#lambda функции, в отличие от обычной, не требуется инструкция return, а в остальном, ведет себя точно так же:

func = lambda *args: args
func(1, 2, 3, 4)
(1, 2, 3, 4)

#==========================

