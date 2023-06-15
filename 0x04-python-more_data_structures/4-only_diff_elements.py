#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    return a set of all elements present in one set
    """
    return ((set_1 | set_2) - (set_1 & set_2))
