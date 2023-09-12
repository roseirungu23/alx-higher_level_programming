#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its content to the standard output """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content) 
