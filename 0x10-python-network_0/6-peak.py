#!/usr/bin/python3
"""You are not allowed to google anything
Whiteboard first
Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Return the peak in a list of integers
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
