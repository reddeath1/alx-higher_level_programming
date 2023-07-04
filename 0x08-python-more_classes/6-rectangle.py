#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on July 4th 21:50:14 2023

@author: Frank Galos
"""


class Rectangle:
    """class Rectangle that define a rectangle figure

    Attributes:
        number_of_instances (int): Number of created rectangles
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializer method for Rectangle

        Attributes:
            width (int, optional): width of the rectangle
            height (int, optional): height of the rectangle
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        str method for  printing rectangle

        Returns:
            string : The string with of rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        Method provides __repr__ method for object rectangle

        Returns:+
            The string (str): string to get
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        """
        delete method for the rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        """
        Getter method Property height to retrieve it

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method height of the rectangle

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Getter method property width to retrieve it

        Returns:
            width (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method  width of the rectangle

        Attributes:
            width (int): The width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        Method to Calculate the area of the rectangle

        Returns:
            Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method that Calculate the perimeter of the rectangle

        Returns:
            Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
