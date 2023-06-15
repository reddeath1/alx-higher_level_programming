#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Delete keys with a specific value in a dictionary
    """
    if a_dictionary is not None and type(a_dictionary) is dict:
        to_delete = {k: x for k, x in a_dictionary.items() if x == value}
        for key, va in to_delete.items():
            del a_dictionary[key]
    return (a_dictionary.copy())
