#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

def pascal_triangle(n):
    """
    Create a pascal triangle

    Attributes:
        n (int): n exponent for triangle

    Return:
         matrix with values for the triangle
    """
    pascal = []
    triangle = []

    for i in range(int(n)):
        new = pascal[:]
        new.append(1)
        pos = len(pascal)
        for x in range(1, pos):
            new[x] = pascal[x - 1] + pascal[x]
        pascal = new[:]
        triangle.append(pascal)
    return triangle
