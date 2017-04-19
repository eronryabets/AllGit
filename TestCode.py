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
    pass


s = "banana"


assert count_vowels(s) == 3
"""
"""
s = "banana"

for i in s:
    print(i, end="")
"""
s = "banana"

i = 0

while i < len(s):
    print(s[i], end="")
    i+=i