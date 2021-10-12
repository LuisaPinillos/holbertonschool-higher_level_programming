#!/usr/bin/python3
"""
MyList that inherits from list
print_sorted prints the list
but sorted
"""


class MyList(list):
    """
    prints the list sorted
    """
    def print_sorted(self):
        print(sorted(self))
