#!/usr/bin/python3
"""
Square class

@author: Frank Galos
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initializer method
        args:
            size: square size
            x: x position
            y: y position
            id: object id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print method
        return:
            formatted list
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x,
                                              self.y, self.width))

    @property
    def size(self):
        """getter width method
        return:
            The size of width and height
        """
        return self.width

    @size.setter
    def size(self, value):
        """The width and height setter method
        args:
            value: The size value
        return:
            no
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square method
        args:
            args: The pointer to arguments
            kwargs: The double pointer
        return:
            no
        """

        if args:
            x = 0
            li = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, li[x], arg)
                x += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary of Square
        return:
            dict
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
