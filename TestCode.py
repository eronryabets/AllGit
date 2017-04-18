# THE MYSTICAL OCTOSPHERE!


import random
import time

# message = ""
#questions = input(str("Задайте свой вопрос магическому Шару...")
time.sleep(1)

def number_to_fortune(num):
    if num == 0:
        return "Да, точно!"

    elif num == 1:
        return "Вероятно, да ..."

    elif num == 2:
        return "Кажется, да ..."

    elif num == 3:
        return "Определенно нет!"

    elif num == 4:
        return "Вероятно, нет"

    elif num == 5:
        return "Я действительно в этом сомневаюсь ..."

    elif num == 6:
        return "Не уверен, зайдите позже!"

    elif num == 7:
        return "Я действительно не могу сказать"

    else:
        return "Я обычный шар, а не предсказатель!"

num = random.randrange(0, 7)
print(number_to_fortune(num))
#TEST#print(number_to_fortune(17))
#time.sleep(3) # zaderzka ispolnenia v 3 sec