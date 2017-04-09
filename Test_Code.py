
"""
def printTwice(bruce):
  print(bruce, bruce)
 printTwice(bruce)
"""
"""
def add(x, y):
    return x + y

print(add(1, 20))
"""

"""Анонимные функции, инструкция lambda
Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее. Анонимные функции
 создаются с помощью инструкции lambda. Кроме этого, их не обязательно присваивать переменной,
 как делали мы инструкцией def func():

 lambda функции, в отличие от обычной, не требуется инструкция return, а в остальном, ведет себя точно так же:

func = lambda x, y: x + y
print(func(1,4))
"""

def catTwice(part1, part2):
    cat = "part1" + "part2"

catTwice("aaa", "bbb")
print(cat)
