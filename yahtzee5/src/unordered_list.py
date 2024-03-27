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

    def get_head(self):
        """ Return the head of the list """
        return self._head

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
        current_node = self.get_head().next
        i = 0
        while current_node is not None:
            if i != index:
                current_node = current_node.next
            else:
                current_node.data = data
                break
            i += 1
        if current_node is None or i > index:
            raise MissingIndex("Index not found!")

    def size(self):
        """
        Get the size of the list
        """
        i = 0
        current_node = self.get_head()

        while current_node.next is not None:
            current_node = current_node.next
            i += 1

        return i

    def get(self, index):
        """
        Return value of index
        """
        current_node = self.get_head().next
        i = 0
        while current_node is not None:
            if i != index:
                current_node = current_node.next
            else:
                break
            i += 1
        if current_node is None or i > index:
            raise MissingIndex("Index not found!")
        return current_node.data

    def index_of(self, value):
        """
        Returns the index of a given value
        """
        current_node = self.get_head().next
        i = 0
        found = False
        while current_node is not None:
            if current_node.data != value:
                current_node = current_node.next
            else:
                found = True
                break
            i += 1
        if found:
            return i
        raise MissingValue("Value not found!")

    def print_list(self):
        """
        Returns the contents of the list
        """
        string = ""
        current_node = self.get_head().next
        while current_node:
            string += str(current_node.data)
            current_node = current_node.next
        print(string)
        return string

    def remove(self, data):
        """
        Remove node with specified data
        """
        previous_node = self.get_head()
        current_node = previous_node.next

        while current_node is not None:
            if current_node.data != data:
                previous_node = current_node
                current_node = current_node.next
            else:
                previous_node.next = current_node.next
                del current_node
                return

        if current_node is None:
            raise MissingValue("Value not found!")

    def __len__(self):
        """
        Get the length of the list
        """
        return self.size()

    def __getitem__(self, key):
        """
        subscriptable method
        """
        return self.get(key)

    def __setitem__(self, key, value):
        """
        item assignment method
        """
        self.set(key, value)
