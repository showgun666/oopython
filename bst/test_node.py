"Module for testing node"
import unittest
from node import Node

class TestNode(unittest.TestCase):
    """
    Submodule for unittests, derives from unittest.TestCase
    """

    def test_init(self):
        """
        Test initialization of Node
        """
        node = Node(5, 'A')
        self.assertEqual(node.key, 5)
        self.assertEqual(node.value, 'A')
        self.assertIsNone(node.parent)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_has_left_child(self):
        """
        Test has_left_child method
        """
        node = Node(5, 'A')
        self.assertFalse(node.has_left_child())
        node.left = Node(3, 'B')
        self.assertTrue(node.has_left_child())

    def test_has_right_child(self):
        """
        Test has_right_child method
        """
        node = Node(5, 'A')
        self.assertFalse(node.has_right_child())
        node.right = Node(7, 'C')
        self.assertTrue(node.has_right_child())

    def test_has_both_children(self):
        """
        Test has_both_children method
        """
        node = Node(5, 'A')
        self.assertFalse(node.has_both_children())
        node.left = Node(3, 'B')
        self.assertFalse(node.has_both_children())
        node.right = Node(7, 'C')
        self.assertTrue(node.has_both_children())

    def test_has_parent(self):
        """
        Test has_parent method
        """
        node = Node(5, 'A')
        self.assertFalse(node.has_parent())
        node.parent = Node(3, 'B')
        self.assertTrue(node.has_parent())

    def test_is_left_child(self):
        """
        Test is_left_child method
        """
        parent = Node(5, 'A')
        node = Node(3, 'B', parent)
        parent.left = node
        self.assertTrue(node.is_left_child())
        parent.right = Node(7, 'C')
        self.assertFalse(parent.right.is_left_child())

    def test_is_right_child(self):
        """
        Test is_right_child method
        """
        parent = Node(5, 'A')
        node = Node(7, 'C', parent)
        parent.right = node
        self.assertTrue(node.is_right_child())
        parent.left = Node(3, 'B')
        self.assertFalse(parent.left.is_right_child())

    def test_is_leaf(self):
        """
        Test is_leaf method
        """
        node = Node(5, 'A')
        self.assertTrue(node.is_leaf())
        node.left = Node(3, 'B')
        self.assertFalse(node.is_leaf())

    def test_lt(self):
        """
        Test __lt__ method
        """
        node1 = Node(5, 'A')
        node2 = Node(3, 'B')
        self.assertTrue(node2 < node1)
        self.assertFalse(node1 < node2)

    def test_gt(self):
        """
        Test __gt__ method
        """
        node1 = Node(5, 'A')
        node2 = Node(3, 'B')
        self.assertTrue(node1 > node2)
        self.assertFalse(node2 > node1)

    def test_eq(self):
        """
        Test __eq__ method
        """
        node1 = Node(5, 'A')
        node2 = Node(5, 'B')
        self.assertTrue(node1 == node2)

if __name__ == '__main__':
    unittest.main()
