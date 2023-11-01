#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = 12
while (res > 9):
    if (number >= 0):
        res = number % 10
    elif (number < 0):
        res = (-number) % 10
if (number < 0):
    res = -res
if (res > 5):
    print(f"Last digit of {number} is {res} and is greater than 5")
elif (res == 0):
    print(f"Last digit of {number} is {res} and is 0")
elif (res < 6 and res != 0):
    print(f"Last digit of {number} is {res} and is less than 6 and is not 0")
