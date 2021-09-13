#!/usr/bin/python3
import random
number = random.randint(0, 10000)
Posnum = 0
lastdig = 0
if number < 0:
    number *= -1
    lastdig = (number % 10)
else:
    Posnum = (number % 10)
if Posnum == 0:
    print("Last digit of: "'{:d}'" is "'{:d}'" and is 0" .format(number, Posnum))
elif Posnum > 5:
    print("Last digit of: "'{:d}'" is "'{:d}'" and is greater than 5" .format(number, Posnum))
else:
    print("Last digit of: "'{:d}'" is "'{:d}'" and is less than 6 and not 0" .format(number, (lastdig)))
