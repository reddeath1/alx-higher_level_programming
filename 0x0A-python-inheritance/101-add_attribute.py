#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def add_attribute(obj, name, value):
    """
    Add attribute into the class if it is possible

    Arguments:
        obj (object): object to set as attribute
        name (str): Name of the new attribute
        value (int): Value to new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
