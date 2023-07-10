#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""


class MyInt(int):
    """
    Class that inherits from int
    """
    def __eq__(self, num):
        """
        equal function for MyInt class

        Attributes:
            num (int): an inputed integer

        Returns:
            The opositive boolean of the input
        """
        return (int(self) != num)

    def __ne__(self, num):
        """
        no equal function for MyInt class

        Attributes:
            num (int): an inputed integer

        Returns:
            The opositive boolean of the input
        """
        return (int(self) == num)
