#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Return a tuple with the length of a string and it first
    character
    """
    count = len(sentence)
    if count == 0:
        first = None
    else:
        first = sentence[0]
    return ((count, first))
