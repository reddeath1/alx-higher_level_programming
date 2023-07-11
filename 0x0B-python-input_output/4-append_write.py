#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def append_write(filename="", text=""):
    """
    Append inputed text into a utf-8 encoded text file

    Arguments:
        filename (str): name of the file to open
        text (str): text to append

    Return:
        File with appened text
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
