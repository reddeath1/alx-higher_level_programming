#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def write_file(filename="", text=""):
    """
    Write inputed text to a utf-8 encoded file

    Arguments:
        filename (str): name of the file to open
        text (str): text to write in

    Return:
        A file with text written in it
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
