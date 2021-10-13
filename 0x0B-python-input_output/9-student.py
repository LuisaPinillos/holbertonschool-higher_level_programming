#!/usr/bin/python3
"""
Write a class Student that defines
a student by and instantiation with
first_name, last_name and age
"""


class Student():
    """
    Create the class Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
