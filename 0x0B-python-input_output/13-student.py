#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        init method for Student class

        Attributes:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Representation of Student class into json format

        Attributes:
            attr (dict): python object to convert

        Return:
            Student class in json format
        """
        if attr is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attr}

    def reload_from_json(self, json):
        """
        Representation of Student class into json format

        Attributes:
            attr (dict): python object to convert

        Return:
            Student class in json format
        """
        for key, value in json.items():
            setattr(self, key, value)
