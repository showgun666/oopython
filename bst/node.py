"Node class for binary search tree"
class Node():
    "Node class"

    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def has_left_child(self):
        "method to check if left child exists"
        return bool(self.left)

    def has_right_child(self):
        "method to check if right child exists"
        return bool(self.right)

    def has_both_children(self):
        "method to check if both children exist"
        return bool(self.left and self.right)

    def has_parent(self):
        "method to check if parent exists"
        return bool(self.parent)

    def is_left_child(self):
        "method to check if self is left child"
        return self.parent and self.parent.left == self

    def is_right_child(self):
        "method to check if self is right child"
        return self.parent and self.parent.right == self

    def is_leaf(self):
        "method to check if self has no children"
        return not (self.left or self.right)

    def __lt__(self, other):
        "method to check if self is less than other"
        return self.key < other

    def __gt__(self, other):
        "method to check if self is greater than other"
        return self.key > other

    def __eq__(self, other):
        "method to check if self is equal to other"
        return self.key == other
