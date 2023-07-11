#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def read_lines(filename="", nb_lines=0):
    """
    Read n lines from file and print to stdout

    Arguments:
        filename (str): name of the file to open
        nb_lines (int): number of lines to print
    """
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
    if nb_lines >= len(lines) or nb_lines <= 0:
        nb_lines = len(lines)
    for x in range(nb_lines):
        print(lines[x], end='')
