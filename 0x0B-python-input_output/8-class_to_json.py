#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def class_to_json(obj):
    """
    Create a json representation of an object

    Arguments:
        obj (obj): The object inputted to create a class

    Return:
        A json representation
    """

    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
