"Binary search tree class"
from node import Node

class BinarySearchTree:
    "binary search tree class"
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        "method for inserting a value into the tree"
        self.root = self.insert_recursive(self.root, key, value, None)

    def insert_recursive(self, node, key, value, parent):
        "method for inserting a value into the tree recursively"
        if node is None:
            return Node(key, value, parent)

        if key < node.key:
            node.left = self.insert_recursive(node.left, key, value, node)
        elif key > node.key:
            node.right = self.insert_recursive(node.right, key, value, node)
        else:
            node.value = value

        return node

    def inorder_traversal_print(self):
        "method for traversing the tree and printing the results"
        self.inorder_traversal_print_recursive(self.root)

    def inorder_traversal_print_recursive(self, node):
        "helper method for recursive inorder traversal"
        if node is not None:
            self.inorder_traversal_print_recursive(node.left)
            print(node.value)
            self.inorder_traversal_print_recursive(node.right)

    def get(self, key):
        "method for getting a value from the tree"
        return self.get_recursive(self.root, key)

    def get_recursive(self, node, key):
        "method for getting a value from the tree recursively"
        if node is None:
            raise KeyError("Key not found in the tree")

        if key == node.key:
            return node.value
        if key < node.key:
            return self.get_recursive(node.left, key)
        return self.get_recursive(node.right, key)

    def remove(self, key):
        "method for removing a value from the tree"
        self.root, removed_value = self.remove_recursive(self.root, key)
        if removed_value is None:
            raise KeyError("Key not found in the tree")
        return removed_value

    def remove_recursive(self, node, key):
        "method for removing a value from the tree recursively"
        if node is None:
            return node, None

        if key < node.key:
            node.left, removed_value = self.remove_recursive(node.left, key)
            if node.left is not None:
                node.left.parent = node
        elif key > node.key:
            node.right, removed_value = self.remove_recursive(node.right, key)
            if node.right is not None:
                node.right.parent = node
        else:
            removed_value = node.value
            if node.left is None:
                if node.right is not None:
                    node.right.parent = node.parent
                return node.right, removed_value
            if node.right is None:
                if node.left is not None:
                    node.left.parent = node.parent
                return node.left, removed_value

            # node with two children, get the successor in order 
            successor = self.find_min(node.right)
            node.key, node.value = successor.key, successor.value
            node.right, _ = self.remove_recursive(node.right, successor.key)
            if node.right is not None:
                node.right.parent = node

        return node, removed_value

    def find_min(self, node):
        "method to find the node with the minimum key"
        current = node
        while current.left is not None:
            current = current.left
        return current

    def size(self):
        "method for size of the tree"
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        "method for recursively getting the size of the tree"
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
