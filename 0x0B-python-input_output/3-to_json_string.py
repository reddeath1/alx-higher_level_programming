#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""
import json

def to_json_string(my_obj):
    """
    Retur a json string containing object's representation

    Arguments:
        my_obj (str): inputed object to convert in json format

    Return:
       json text format
    """
    return json.dumps(my_obj)
