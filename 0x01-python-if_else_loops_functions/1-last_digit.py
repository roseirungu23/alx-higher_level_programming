#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
if number < 0:
    lastd = -lastd
if lastd > 5:
    print("Last digit of", number, "is", lastd, "and is greater than 5")
elif lastd == 0:
    print("Last digit of", number, "is", lastd, "and is 0")
else:
    print("Last digit of", number, "is", lastd, "and is less than 6 and not 0")
