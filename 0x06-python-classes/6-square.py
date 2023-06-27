#!/usr/bin/python3

class Square:
    """Class that has attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int', optional): A public instance size
            position: (:obj: 'tuple', optional): public instance position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Call the function to check the property

        Returns:
            The size of the square
        """
        return self.__size

    @property
    def position(self):
        """Call the function to check the property

        Returns:
            The tuple position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """check the errors and setter for the size attribute

        Args:
            value: Value to check the errors

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """check the errors and setter for the size attribute

        Args:
            value: Value to check the errors

        Raises:
            TypeError: Exception if size is not an integer
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # character
        """

        if self.__size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.size):
                for v in range(self.position[0]):
                    print(end=" ")
                for b in range(self.size):
                    print("#", end="")
                print()
