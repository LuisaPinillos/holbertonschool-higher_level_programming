#!/usr/bin/python3
"""
MyList that inherits from list
print_sorted prints the list
but sorted
"""


class MyList(list):
    def print_sorted(self):
        """
        prints the list sorted
        """
        print(sorted(self))
