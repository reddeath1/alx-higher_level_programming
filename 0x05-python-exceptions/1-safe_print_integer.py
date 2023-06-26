#!/usr/bin/python3

def safe_print_integer(value):
    """
    print the list only  integers
    Return the amount of integers printed
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
