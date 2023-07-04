#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""

class LockedClass:
    """A locked class that only let the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
