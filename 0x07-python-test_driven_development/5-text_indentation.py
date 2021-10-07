#!/usr/bin/python3
"""
prints a text with 2 new lines
after the specific characters
., ? and :
"""


def text_indentation(text):
    """text must be a string"""

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == ".":
            print(".\n")
        elif text[i] == "?":
            print('?\n')
        elif text[i] == ":":
            print(":\n")
        else:
            if (text[i] == " " and (text[i - 1]
                                    in ".?:" or text[i - 1] == " ")):
                continue
            print("{}".format(text[i]), end="")
