#!/usr/bin/python3

def no_c(my_string):
    """
    remove all characters 'c' and 'C' from s
    """
    str = ""
    for i in my_string:
        if i not in "cC":
            str += i
    return (str)
