"""
Denna modul innehåller en klass som simulerar en unordered list
Detta är för att lära mig datastrukturer.
"""
from src.node import Node

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
        ...

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
