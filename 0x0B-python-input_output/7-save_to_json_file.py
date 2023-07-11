#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save object to a file

    Arguments:
        my_obj (obj): inputed object to convert in json format
        filename (str): name of the output file

    Return:
        file with a text in jason format
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
