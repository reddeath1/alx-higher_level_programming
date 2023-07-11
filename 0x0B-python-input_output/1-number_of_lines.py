#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def number_of_lines(filename=""):
    """
    Count the number of lines from the filename

    Arguments:
        filename (str): A name of the file to count in
    """
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
    return len(lines)
