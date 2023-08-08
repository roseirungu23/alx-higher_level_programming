#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
lastdig = abs(num) % 10
if num < 0:
    lastdig = -lastdig
if lastdig > 5:
    print("Last digit of", num, "is", lastdig, "and is greater than 5")
elif lastdig == 0:
    print("Last digit of", num, "is", lastdig, "and is 0")
else:
    print("Last digit of", num, "is", lastdig, "and is less than 6 and not 0")
