#!/usr/bin/python3
"""
Class Module

@author: Frank Galos
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializer method

        args:
            width: width of a rectangle
            height: height of a rectangle
            x: init variable
            y: init variable
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """return the area of width & height"""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """update the attributes"""
        if args:
            li = ['id', 'width', 'height', 'x', 'y']
            x = 0
            for arg in args:
                setattr(self, li[x], arg)
                x += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """print into stdout
        return: no
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """print method"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def to_dictionary(self):
        """return dict representation of Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """getter with method"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter with  method"""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """getter height method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height method"""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """getter x method"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x method"""
        self.integer_validator2('x', value)
        self.__x = value

    @property
    def y(self):
        """getter y method"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y method"""
        self.integer_validator2('y', value)
        self.__y = value
