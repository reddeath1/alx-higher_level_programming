#!/usr/bin/python3

def safe_function(fct, *args):
    """
    execute a function safely and return the result of the function
    """
    try:
        r = fct(*args)
        return r
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
