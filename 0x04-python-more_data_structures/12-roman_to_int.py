#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    convert a roman numeral character into the respective integer
    """
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    roman_list = list(roman_string.upper())
    results = 0
    prev = 0
    for s in roman_list:
        if s in roman_dictionary:
            results += roman_dictionary[s]
            if roman_dictionary[s] > prev:
                results -= prev * 2
            prev = roman_dictionary[s]
        else:
            return (0)
    return (results)
