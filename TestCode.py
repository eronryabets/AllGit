"""
print("Проверка четности числа")
number = int(input("Введите ваше число "))
if number%2 == 0:
    print(number, " число четное")
else: print(number, " число не четное")
"""
"""
def atom(number):
    if number % 2 == 0:
        print(number, " число четное")
    else:
        print(number, " число не четное")


print(atom(int(input("введите число "))))
"""
"""
number = int(input("input your numbers "))
if 0 <= number <= 13:
    print(number, "Ha ha ha")
else:
     number > 13
     print("ok")
if number > 15:
    print("No")


#print(10 < 20 < 30)

"""
"""
number = int(input("input your numbers "))
if 0 <= number <= 30:
    print(number, "first")
elif 31 <= number <= 60:
    print("second")
else:
    number > 61
    print("Third")
"""



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
