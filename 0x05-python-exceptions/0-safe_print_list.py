#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints the list of anything, but only print the integers
    Return the amount of integers printed
    """
    result = 0
    for v in range(x):
        try:
            print("{:d}".format(my_list[v]), end="")
            result += 1
        except:
            continue
    print()
    return result
