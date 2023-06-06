#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number

if number < 0:
    number = -(number)

lastNum = number % 10
if num < 0:
    number = num
    lastNum = -(lastNum)

if lastNum > 5:
    string = "and is greater than 5"
elif lastNum == 0:
    str = "and is 0"
elif lastNum < 6:
    str = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, lastNum), str)
