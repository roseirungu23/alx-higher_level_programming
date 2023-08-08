#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if lastdigit > 5:
    output = "and is greater than 5"
elif lastdigit == 0:
    output = "and is 0"
else:
    output = "and is less than 6 and not 0"
    print("Last digit of", number, "is", lastdigit, output)
