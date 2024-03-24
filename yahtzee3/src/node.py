"""
Detta är en modul för att simulera en nod
för att lära mig datstrukturer.
Används av unorderedList
"""

class Node():
    """
    Node class
    """

    def __init__(self, data, next_=None):
        """
        Initialize object with data and next set to None.
        Next will be assigned when new data is added.
        """
        self.data = data
        self.next = next_
