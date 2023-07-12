#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""
import json

def load_from_json_file(filename):
    """
    Load an object from json file

    Arguments:
        filename (str): name of the output file

    Return:
        file with a text in jason format
    """
    with open(filename, encoding='utf-8') as file:
        return (json.loads(file.read()))
