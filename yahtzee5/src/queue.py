"""
This module contains the Queue class
"""
class Queue:
    "Cueue class"
    def __init__(self):
        self._items = []

    def is_empty(self):
        "Check if empty method"
        return not self._items

    def enqueue(self, item):
        "Enqueue method"
        self._items.append(item)

    def dequeue(self):
        "Dequeue method"
        try:
            return self._items.pop(0)

        except IndexError:
            return "Empty list."

    def peek(self):
        "Peek method"
        return self._items[0]

    def size(self):
        "size method"
        return len(self._items)

    def to_list(self):
        "To list method"
        arr = []
        i = self.size()
        while i > 0:
            self.enqueue(self.peek())
            arr.append(self.dequeue())
            i -= 1
        return arr
