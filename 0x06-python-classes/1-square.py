#!/usr/bin/python3

class Square:
    """Class that has attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int'): private instance size
        """
        self.__size = size
