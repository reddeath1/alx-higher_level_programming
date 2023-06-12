#!/usr/bin/python3

def element_at(my_list, index):
    """
    Get an element in a list at given index
    And return it
    """
    if index >= len(my_list) or index < 0:
        return

    return (my_list[index])
