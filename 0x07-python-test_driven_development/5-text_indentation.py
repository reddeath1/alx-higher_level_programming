#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def text_indentation(text):
    """
    print the string with 2 new lines after '.', '?', and ':'

    Args:
        text (int): text to print

    Raises:
        TypeError: "text must be a string"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    str = text.replace('.', '.\n\n').replace(':', ':\n\n')\
        .replace('?', '?\n\n')
    for i in range(len(text)):
        str = string.replace('\n ', '\n')

    print(str, end='')
