#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    list = load_from_json_file('add_item.json')
except:
    list = []

for x in range(1, len(sys.argv)):
    list.append(sys.argv[x])

try:
    save_to_json_file(list, 'add_item.json')
except:
    pass
