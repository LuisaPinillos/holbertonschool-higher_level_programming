#!/usr/bin/python3
"""
Function that appends
a string at the end
of a text file
"""


def append_write(filename="", text=""):
    """
    Returns the number of characters written.
    """
    with open(filename, 'a') as f:
        return f.write(text)
