#!/usr/bin/python3
"""Defines function text_indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these
        characters: ., ? and :"""
    Args:
        text(str): The input text.

    Raises:
        TypeError: If text is not a string.
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        char = 0
        while char < len(text) and text[char] == '':
            char += 1

        while char < len(text):
            print(text[char], end="")
            if text[char] == "\n" or text[char] in ".?:":
                if text[char] in ".?:":
                    print("\n")
                char += 1
                while char < len(text) and text[char] == '':
                    char += 1
                continue
            char += 1
