#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

class Student:
    """
    The Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        initializer method for Student class

        Attributes:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Represent of Student class into json format

        Return:
            Student class as a json format
        """
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
