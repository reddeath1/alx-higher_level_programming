#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

class BaseGeometry():
    """
     empty class
    """
    pass

    def area(self):
        """
        Public instance method that calculate the area

        Raises:
            Exception if area is not imlemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validate integer input
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
