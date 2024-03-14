"""
Denna modul innehåller en klass som simulerar en unordered list
Detta är för att lära mig datastrukturer.
"""
from src.node import Node
from src.errors import MissingIndex
from src.errors import MissingValue

class UnorderedList():
    """
    Unordered List class
    """
    def __init__(self):
        """
        Initiate a new unordered list instance
        """
        self._head = Node(1) # Head is a node
        self._tail = self._head # An empty list's tail is also the head

    def append(self, data):
        """
        Append data to the end of the unordered list.
        """
        self._tail.next = Node(data)
        self._tail = self._tail.next

    def set(self, index, data):
        """
        Set the value of a given index in the list
        """
        current_node = self._head.next
        i = 0
        while current_node != None:
            if i == index:
                current_node.data = data
                break
            else:
                current_node = current_node.next
            i += 1
        if current_node == None or i > index:
            raise MissingIndex("Index not found!")

    def size(self):
        """
        Get the size of the list
        """
        i = 0
        current_node = self._head

        while current_node.next != None:
            current_node = current_node.next
            i += 1

        return i
    
    def get(self, index):
        """
        Return value of index
        """
        current_node = self._head.next
        i = 0
        while current_node != None:
            if i == index:
                return current_node.data
            else:
                current_node = current_node.next
            i += 1
        if current_node == None or i > index:
            raise MissingIndex("Index not found!")

    def index_of(self, value):
        """
        Returns the index of a given value
        """
        current_node = self._head.next
        i = 0
        while current_node != None:
            if current_node.data == value:
                return i
            else:
                current_node = current_node.next
            i += 1
        raise MissingValue("Value not found!")

    
    def print_list(self):
        """
        Returns the contents of the list
        """
        string = ""
        current_node = self._head.next
        while current_node:
            string += str(current_node.data).strip("'").strip("(").strip(")").strip(" ") + "\n"
            current_node = current_node.next
        return string[:-1]
    
    def remove(self, data):
        """
        Remove node with specified data
        """
        previous_node = self._head
        current_node = self._head.next

        while current_node != None:
            if current_node.data == data:
                previous_node.next = current_node.next
                del current_node
                return
            else:
                previous_node = current_node
                current_node = current_node.next
        if current_node == None:
            raise MissingValue("Value not found!")
