#-*- coding: utf-8 -*-

"""
#str.upper()
s= "abc
s.upper()
"""
"""

s = "12345"
print(len(s))
"""

"""
print(" a".strip())
"""

"""
s = " John"
" a".lstrip().rstrip() #ybiraet probeli v texte
#"b ".rstrip()
#s[0].isupper()
"""
"""
email = "john@gmail.com"

#i = x.find("@")
#name = x[:4]   # operator slith

i = email.find("@")
#print(i)
name = email[:i]      #i = 4, 4ka eto nomer @ poschety do silmvolov
print(name)

#if i < 0:     #esli index -1 to vernem pystyy stroky
#    name = ""
#else:
#    name = email[:i}

assert name == "john"

assert email[:email.find("@")] == "john"

"""
"""
#s[-1] - vertnet posledniy simvol stroki
s = "abc"
s.find("d") # vozvrshaet -1 (== -1 True)
#esli Find ne ydalos naitit simvol on vernet -1
"""
"""
text1 = "this is a sentence."
text2 = "This is a question?"

#print(text1[-1])

last = text1[-1]
#text2[-2]

if last == "?":
    print("Question")
else:
    print("Asset")
"""
"""
s = "Question"
#s[:] polychim kopiy ishodnoi stroki - vse simvoli
#print([s])
"""
"""
empty = ""
empty[:]
"""
"""
def count_vowels(s):
    


s = "banana"


assert count_vowels(s) == 3
"""
"""
s = "banana"

for i in s:
    print(i, end="")
"""
"""
s = "banana"

i = 0

lenght = len(s)
#while i < len(s):
while i < lenght:
    print(s[i], end="")
    i+=1
"""
"""
s = "abc"
#"a" prinadlegit li "abc"


if "abc".find("a") <0:
    print("No") # esli net simvola to vernet -1
else:
    print("Yes")
"""
"""
"a" in "abc" #True
"""

"d" in "aeiou" #tak glasnie vichiclit
"""
"""
"""
s = "banana"

i = 0

lenght = len(s)
#while i < len(s):
while i < lenght:
    print(s[i], end="")
    i+=1

"""

"""

def count_vowels(s):
    i = 0
    lenght = len(s)
    count = 0
    # while i < len(s):
    while i < lenght:
        if s[i] in "aeiou":
            count += 1
        else:
            pass
        i += 1
    return count


s = "banana"


assert count_vowels(s) == 3



"""
"""

def count_vowels(s):
    i = 0
    lenght = len(s)
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count


s = "banana"


assert count_vowels(s) == 3
"""
"""

def count_volwes(s):
    return len(list(filter(lambda x: x in "aeiou" , s)))

s = "banana"

assert count_volwes(s) == 3

#%timeit count_volwes(s)

#print(len(list("aaa")))
"""
"""

s = "abba"


substr = "ab"
#S.rindex(str, [start],[end])

print(s.rfind("ab"))

LECTURE 9 =======================================================
"""
"""
A = [1, 2, 3, 4, 5]
B = [2, 3]

print(list(set(A) - set(B)))

"""
"""
#SET

#index - on je klych

x = [1, 3, 2, 3, 5]
print(list(set(x)))

"""
"""
#korteji - ne izmenyaemie - a tak oni pohozi na spiski ( rabota s nimi bolee bistra)

x = 10
y = 20
#swap x, y = y, x
"""
"""
x = 1,2 #1,2 eto tuples
print(x)
"""
"""
x = 1, 2, 3, "a"
print(x[3])

"""
"""

# Пример создания словаря перевода английских слов на испанский язык
eng2sp = {} # создаем пустой словарь с именем eng2sp
eng2sp['one'] = 'uno' # добавляем очередной элемент в словарь
eng2sp['two'] = 'dos' # добавляем очередной элемент в словарь

"""
"""

eng2sp = dict(one="uno",
              two="dos",
              three="tres")
"""
"""
#elementi iz slovara polychaytsa po klychy

print(eng2sp["two"])
"""

"""
day_weeks = {"1" : "PN",
            "2" : "VT",
            "3" : "SR"}
print(day_weeks["2"])

"""
#klych v slovare perezapisivat nelza - ego mozno libo ydait libo dobavit

"""
L = []
D = {"a" : 10}

L.append(D)
#print(L)

D["a"] = 42
L.append(D)

print(L)

#piton hranit dannie po ssilke - variant sozdat copy

"""

