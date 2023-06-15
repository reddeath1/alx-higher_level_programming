#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    update or add key/value into a dictionary and return a new copy
    """
    a_dictionary.update({key: value})
    return (a_dictionary.copy())
