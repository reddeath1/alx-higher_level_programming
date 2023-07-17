#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Frank Galos
"""
import json


class Base:
    """
    Class Base

    Attributes:
        nb_objects (int): Private class attribute
    """
    __objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Attributes:
            id (int): The integer input for id
        """
        if id is None:
            Base.__objects += 1
            self.id = Base.__objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return a json string representation

        Attributes:
            list_dictionaries (json): The inputted jason list of dictionaries
        Return:
            The json repreentation
        """
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the json string repressentation list object to a file

        Attribute:
            list_objs (list): The object list to save

        Return:
            json object to save in file
        """
        file_name = cls.__name__ + ".json"
        str = []
        if list_objs is not None:
            for x in list_objs:
                str.append(cls.to_dictionary(i))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(str))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of json string representation

        Attribute:
            json_string (string): The json object

        Return:
            json object to dictionary
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set

        Attribute:
            dictionary (dict): The inooutted dictionary

        Return:
            An instance with all attributers already set
        """
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        if cls.__name__ == "Square":
            dum = cls(1)
        dummy.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances

        Return:
            A list of instances
        """
        file_name = cls.__name__ + ".json"
        json_obj = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                json_obj = cls.from_json_string(file.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except:
            pass
        return json_obj
