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
            raise MissingIndex("Index not found!")

    def size(self):
        """
        Get the size of the list
        """
        i = 0
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            i += 1

        return i
    
    def get(self, index):
        """
        Return value of index
        """
        current_node = self.head.next
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
        current_node = self.head.next
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
        Prints the contents of the list
        """
        list_contents = ""
        current_node = self.head.next
        while current_node != None:
            list_contents += str(current_node.data) + "\n"
            current_node = current_node.next
        print(list_contents)
    
    def remove(self, data):
        """
        Remove node with specified data
        """
        previous_node = self.head
        current_node = self.head.next

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
