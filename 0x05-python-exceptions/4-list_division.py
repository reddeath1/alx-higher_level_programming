#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    take two lists and create a new list with result of divison operation
    handles errors and prints them to stdout
    """
    list = []
    results = 0
    for i in range(0, list_length):
        try:
            results = (my_list_1[i] / my_list_2[i])
        except TypeError:
            results = 0
            print("wrong type")
        except ZeroDivisionError:
            results = 0
            print("division by 0")
        except IndexError:
            results = 0
            print("out of range")
        finally:
            list.append(results)
    return list
