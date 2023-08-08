#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        else:
            print("{:s}".format(char),end="")
    print()
