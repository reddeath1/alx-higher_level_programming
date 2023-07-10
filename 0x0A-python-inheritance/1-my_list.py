#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""


class MyList(list):
    """
     MyList class that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that print sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
