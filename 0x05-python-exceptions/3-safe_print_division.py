#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divide two integers and print the result
    catches divide by zero exception
    """
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
