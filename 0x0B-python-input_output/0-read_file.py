#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def read_file(filename=""):
    """
    Read the file

    Arguments:
        filename (str): A name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
