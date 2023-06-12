#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    find all multiples of 2 in a list and return
    True or False list
    """
    len_l = len(my_list)
    if len_l == 0:
        return None

    l = []
    for i in my_list:
        if i % 2 == 0:
            l.append(True)
        else:
            l.append(False)
    return (l)
