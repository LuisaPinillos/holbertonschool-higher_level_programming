#!/usr/bin/python3
"""
Function that writes a string
to a text file and 
"""

def write_file(filename="", text=""):
    """
    Returns the number of characters written:
    """
    with open(filename, 'w') as f:
        return f.write(text)
