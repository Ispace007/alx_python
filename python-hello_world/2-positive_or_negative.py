import random
number = random.randint(-10, 10)
x = int(input("Value:"))
if x>0 :
    print(x, "is positive")
elif x == 0 :
    print(x, "is zero")
else:
    print(x, "is negative")