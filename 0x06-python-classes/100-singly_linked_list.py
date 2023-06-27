
#!/usr/bin/python3
""" Declare the Node module class """


class Node:

    def __init__(self, data, next_node=None) -> None:
        """
        Intializes the attributes of node class

        Args:
            data: value of node
            next_node:  The address of next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Get the data of the linked list """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Get the next_node of the linked list """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Declare a class of SinglyLinkedList """

    def __init__(self) -> None:
        """ Intializes the private attribute """
        self.__head = None

    def __str__(self) -> str:
        """ return string to be printed for SinglyLinkedList """
        output = list()
        next = self.__head

        while next is not None:
            output.append(str(future.data))
            next = future.next_node

        return "\n".join(output)

    def sorted_insert(self, value):
        """
        Sorts the node values

        Args:
            value: The  value of node
        """
        if self.__head is None:
            self.__head = Node(value)
            return

        if value < self.__head.data:
            self.__head = Node(value, self.__head) 
            return

        next, prev = self.__head.next_node, self.__head
        while next is not None:
            if value < future.data:
                prev.next_node = Node(value, next)
                return
            prev = next
            next = prev.next_node
        prev.next_node = Node(value)

