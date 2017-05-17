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
"""
x = "b"

#keys spicok vivedet klychei

if x in D.keys():
    print(D[x])
"""
"""
vowels = {"a", "e", "i", "o", "u"}

word = "hello"

count = 0
for ch in word :
   if ch in vowels:
       count += 1

print(count)
"""
"""
x = "a"

if x in D:
    print(D[x])

"""

"""




corpus = ["slovo", "slovo", "slovo2"]

hist = dict()

for word in corpus:
    if word in hist:
        hist[word] += 1
    else:
        hist[word] = 1

print(hist)
assert sum(hist.values()) == len(corpus)

#sartirovka slovara po klychy nevozmozna
#items vozrasaet spisok - a ego mozna otsortirovat yje

sorted(hist.items(), key=lambda x: x[1]) #x - eto kajdiy kortej v etom spiske


"""
#17 мая

"""



class Point:
    pass

blank = Point()
print(type(blank))

#sinstansiirovali Class/ obiavili noviy tip dannih


"""

"""
#blak = Point()
# blank = Point__init__

class Point:
    def __init__(self, x=0, y=0 ):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


    def show_point(self):
        print("({}, {})".format(self.x, self.y))


blank = Point() # Point.__init__()
p1 = Point(2, 3) # Point.__init__(x=2, y=3)
p2 = Point(3, 4) # Point.__init__(x=2, y=3)

p1.show_point() # Point.show_point(p1)

#p1. posle to4ki imya obiecta i ego vizov
# self - prosto imya peremennoi - "ykazatel na sebya"

print(p1) #print(Point.__str__(p1))


"""

class Boat:
    def __init__(self, name, start=0, finish=0):
        self.name = name
        self.start = start
        self.finish = finish


    def __str__(self):
        return "{}".format(self.name)

    def get_duration(self):
        return self.finish - self.start

class Navy:
    def __init__(self, boats=[]):
        self.boats = boats

    def __str__(self):
        pass
    def get_average(selfself):
        return sum(map(lambda x: x.get_duration(), self.boats))/len(self.boats)

    def get_max_duration(self):
        return sum(map(lambda x: x.get_duration(), self.boats))/len(self.boats)

navy = Navy([Boat("first", 10, 30),
             Boat("second", 15, 25),
             Boat("third", 5, 20)])

#print(sum(map(lambda x: x.finish - x.start, boats))/len(boats))
#print(sum(map(lambda x: x.get_duration(), boats))/len(boats))

