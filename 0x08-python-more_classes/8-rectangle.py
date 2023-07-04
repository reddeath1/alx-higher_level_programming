#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue July 04 22:15:14 2023

@author: Frank Galos
"""

class Rectangle:
    """class Rectangle that define a rectangle figure

    Attributes:
        number_of_instances (int): Number of created rectangles
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializer method for Rectangle

        Attributes:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectangle
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        str method to print rectangle

        Returns:
            string : string with # rectangle
        """
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str

        for i in range(self.__height):
            for j in range(self.__width):
                str += str(self.print_symbol)
            if i < self.__height - 1:
                str += '\n'
        return str

    def __repr__(self):
        """
        provide __repr__ method for object rectangle

        Returns:+
            string (str): string to get
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        """
        delete method for rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height (int): height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method height of the rectangle

        Attributes:
            height (int): height of the rectangle

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
        getter Property width to retrieve it

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
            area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method to Calculate the perimeter of the rectangle

        Returns:
            perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        The Method to compare 2 rectangles

        Attributes:
            rect_1 (class Rectangle): Rectangle 1 must be an instance rectangle
            rect_2 (class Rectangle): Rectangle 2 must be an instance rectangle

        Raises:
            TypeError: If rect_1 or rect_2 aren't instance of rectangle

        Returns:
            biggest rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
