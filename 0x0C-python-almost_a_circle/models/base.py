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

     @classmethod
     def save_to_file_csv(cls, list_objs):
        file = cls.__name__ + ".csv"
        with open(file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        file = cls.__name__ + ".csv"
        try:
            with open(file, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                obj_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle" and len(row) == 5:
                        obj_dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square" and len(row) == 4:
                        obj_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                    else:
                        continue
                    obj_list.append(cls.create(**obj_dict))
                return obj_list
        except FileNotFoundError:
            return []

     @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.setup(800, 600)
        screen.title("Drawing Rectangles and Squares")

        drawer = turtle.Turtle()

        def draw_rectangle(x, y, width, height):
            drawer.penup()
            drawer.goto(x, y)
            drawer.pendown()
            for _ in range(2):
                drawer.forward(width)
                drawer.left(90)
                drawer.forward(height)
                drawer.left(90)

        def draw_square(x, y, size):
            draw_rectangle(x, y, size, size)

        drawer.speed(1)

        drawer.color("blue")

        for rectangle in list_rectangles:
            x = rectangle.x
            y = rectangle.y
            width = rectangle.width
            height = rectangle.height
            draw_rectangle(x, y, width, height)

        drawer.color("red")

        for square in list_squares:
            x = square.x
            y = square.y
            size = square.size
            draw_square(x, y, size)

        screen.exitonclick()

