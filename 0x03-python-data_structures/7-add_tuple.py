#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    add the first two elements of two tuples together
    and return the result
    """
    count_a = len(tuple_a)
    count_b = len(tuple_b)
    tuple = ()
    for x in range(2):
        if x >= count_a:
            a = 0
        else:
            a = tuple_a[x]
        if x >= count_b:
            b = 0
        else:
            b = tuple_b[x]

        if (x == 0):
            tuple = (a + b)
        else:
            tuple = (tuple, a + b)
    return (tuple)
