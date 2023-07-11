#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line after each line containing a specific string

    Arguments:
        filename (str): name of the file
        search_string (str): string to math
        new_string (str): string to insert after matching
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        contents = "".join(lines)
        file.write(contents)
