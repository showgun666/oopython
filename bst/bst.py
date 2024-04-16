"Binary search tree class"
from node import Node

class BinarySearchTree():
    "binary search tree class"
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        "method for inserting a value into the tree"
        self.root = self.insert_recursive(self.root, key, value, None)

    def insert_recursive(self, node, key, value, parent):
        "method for inserting a value into the tree recursively"
        if node is None:
            new_node = Node(key, value, parent)
            return new_node

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
        return removed_value

    def remove_recursive(self, node, key):
        "method for removing a value from the tree recursively"
        if node is None:
            return node, None

        if key < node.key:
            updated_left, removed_value = self.remove_recursive(node.left, key)
            node.left = updated_left
            return node, removed_value
        if key > node.key:
            updated_right, removed_value = self.remove_recursive(node.right, key)
            node.right = updated_right
            return node, removed_value
        # Node to be removed found
        removed_value = node.value

        if node.left is None:
            temp = node.right
            del node
            return temp, removed_value
        if node.right is None:
            temp = node.left
            del node
            return temp, removed_value
        # Node has both children
        successor_parent = node
        successor = node.right
        while successor.left is not None:
            successor_parent = successor
            successor = successor.left

        if successor_parent != node:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

        node.key = successor.key
        node.value = successor.value

        del successor
        return node, removed_value

    def size(self):
        "method for size of the tree"
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        "method for recursively getting the size of the tree"
        if node is None:
            return 0
        left_size = self._size_recursive(node.left)
        right_size = self._size_recursive(node.right)
        return left_size + right_size + 1
