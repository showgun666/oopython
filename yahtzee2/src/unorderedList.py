"""
Denna modul innehåller en klass som simulerar en unordered list
Detta är för att lära mig datastrukturer.
"""
from src.node import Node
from src.errors import MissingIndex

class UnorderedList():
    """
    Unordered List class
    """
    def __init__(self):
        """
        Initiate a new unordered list instance
        """
        self.head = Node(1)

    def append(self, data):
        """
        Append data to the end of the unordered list.
        """
        current_node = self.head

        # Point current_node to the next node in the list until it points to None
        while current_node.next != None:
            current_node = current_node.next

        # Point the current node to a new node with the data to be appended to the list.
        current_node.next = Node(data)

    def set(self, index, data):
        """
        Set the value of a given index in the list
        """
        current_node = self.head.next
        i = 0
        while current_node != None:
            if i == index:
                current_node.data = data
                break
            else:
                current_node = current_node.next
            i += 1
        if current_node == None or i > index:
            raise MissingIndex("Index out of range!")

    def size(self):
        ...
    
    def get(self, index):
        ...
    
    def index_of(self, value):
        ...
    
    def print_list(self):
        ...
    
    def remove(self, data):
        ...
