#!/usr/bin/python3
"""
Class Module

@author: Frank Galos
"""
import json


class Base:
    """ base class
    Attributes:
        _nb_objects: The number of objects created
        id: id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initiation method
        args:
            id: id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """check if it's an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def integer_validator2(self, name, value):
        """check if  it's an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string
        args:
            list_dictionaries:The list of dictionaries
        return:
            return serialized list
        """
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(str):
        """json to string static method
        args:
            str: json object string type
        return:
            list of json string
        """
        if str:
            return json.loads(str)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """write a JSON string to a file
        args:
            list_objs: list of objects
        return:
            na
        """
        if list_objs:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            j = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(j)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes set
        args:
            dictionary: The double pointer
        return:
            instance with set attribute
        """
        if cls.__name__ == "Rectangle":
            dummy_data = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_data = cls(1)
        dummy_data.update(**dictionary)
        return dummy_data

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances
        return:
            list of instance json of string
        '''
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                d = cls.from_json_string(f.read())
            return [cls.create(**x) for x in d]
        except FileNotFoundError:
            return []
