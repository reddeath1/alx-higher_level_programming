#!/usr/bin/python3

def best_score(a_dictionary):
    """
    return the best value from a dictionary (greatest integer)
    """
    max_value = 0
    greatest = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                greatest = key
    return greatest
