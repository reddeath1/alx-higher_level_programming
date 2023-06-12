#!/usr/bin/python3

def replace_in_list(my_list, idx, el):
    """
    Replace an element in a list at given index
    """
    if len(my_list) <= idx or idx < 0:
        return (my_list)

    my_list[idx] = el
    return (my_list)
