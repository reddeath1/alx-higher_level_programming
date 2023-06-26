#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    print list of only integers
    Return the amount of integers
    """
    result = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            result += 1
        except (ValueError, TypeError):
            continue
    print()
    return result
