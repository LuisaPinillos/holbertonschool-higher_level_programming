#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = 0
if number >= 0:
    lastdig = (number % 10)
else:
    lastdig = (number % -10)
print("Last digit of: ", number, "is ", lastdig, end =' ')
if (number % 10) == 0:
    print("and is 0")
elif number > 5:
        print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
