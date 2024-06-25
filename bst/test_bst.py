"Modeule for testing bst"
import unittest
import sys
from io import StringIO
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    """
    Submodule for unittests, derives from unittest.TestCase
    """

    def test_insert(self):
        """
        Test insertion into the tree
        """
        bst = BinarySearchTree()
        bst.insert(10, 'A')
        bst.insert(5, 'B')
        bst.insert(15, 'C')
        bst.insert(3, 'D')
        bst.insert(7, 'E')
        bst.insert(12, 'F')
        bst.insert(17, 'G')

        self.assertEqual(bst.root.key, 10)
        self.assertEqual(bst.root.left.key, 5)
        self.assertEqual(bst.root.right.key, 15)
        self.assertEqual(bst.root.left.left.key, 3)
        self.assertEqual(bst.root.left.right.key, 7)
        self.assertEqual(bst.root.right.left.key, 12)
        self.assertEqual(bst.root.right.right.key, 17)

    def test_inorder_traversal_print(self):
        """
        Test inorder traversal and printing
        """
        bst = BinarySearchTree()
        bst.insert(10, 'A')
        bst.insert(5, 'B')
        bst.insert(15, 'C')
        bst.insert(3, 'D')
        bst.insert(7, 'E')
        bst.insert(12, 'F')
        bst.insert(17, 'G')

        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            bst.inorder_traversal_print()
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        expected_output = "D\nB\nE\nA\nF\nC\nG\n"
        self.assertEqual(output, expected_output)

    def test_get(self):
        """
        Test getting a value from the tree
        """
        bst = BinarySearchTree()
        bst.insert(10, 'A')
        bst.insert(5, 'B')
        bst.insert(15, 'C')
        bst.insert(3, 'D')
        bst.insert(7, 'E')
        bst.insert(12, 'F')
        bst.insert(17, 'G')

        self.assertEqual(bst.get(10), 'A')
        self.assertEqual(bst.get(3), 'D')
        self.assertEqual(bst.get(15), 'C')
        self.assertEqual(bst.get(7), 'E')
        self.assertEqual(bst.get(12), 'F')
        self.assertEqual(bst.get(17), 'G')

    def test_remove(self):
        """
        Test removing a value from the tree
        """
        bst = BinarySearchTree()
        key_values = [5, 2, 10, 7]

        for i in key_values:
            bst.insert(i, str(i))

        self.assertEqual(bst.root.value, "5")
        self.assertEqual(bst.root.right.value, "10")
        self.assertEqual(bst.root.right.left.value, "7")
        self.assertEqual(bst.remove(7), "7")
        self.assertIsNone(bst.root.right.left)

    def test_remove_and_keep_bst_integrity(self):
        """
        Bst integrity remains after removing nodes
        """
        bst = BinarySearchTree()
        nodes = [9, 5, 2, 15, 4, 3, 11, 12, 10, 0, 1, 14, 16, 7, 8, 6]
        removal = [5, 0, 2, 3, 14, 16, 4, 15, 1, 6, 12, 10, 7, 11, 8, 9]

        for node in nodes:
            bst.insert(node, str(node))

        for key in removal:
            bst.remove(key)
            if bst.root is not None:
                if bst.root.left:
                    self.assertLess(bst.root.left.key, bst.root.key)
                if bst.root.right:
                    self.assertGreater(bst.root.right.key, bst.root.key)

    def test_remove_keeps_bst_integrity_on_root_removal(self):
        """
        Bst integrity remains after removing root repeatedly
        """
        bst = BinarySearchTree()
        nodes = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]
        for node in nodes:
            bst.insert(node, str(node))

        for node in nodes:
            bst.remove(bst.root.key)
            if bst.root is not None:
                if bst.root.left:
                    self.assertLess(bst.root.left.key, bst.root.key)
                if bst.root.right:
                    self.assertGreater(bst.root.right.key, bst.root.key)

    def test_size(self):
        """
        Test getting the size of the tree
        """
        bst = BinarySearchTree()
        bst.insert(10, 'A')
        bst.insert(5, 'B')
        bst.insert(15, 'C')
        bst.insert(3, 'D')
        bst.insert(7, 'E')
        bst.insert(12, 'F')
        bst.insert(17, 'G')

        self.assertEqual(bst.size(), 7)

    def test_insert_works(self):
        """
        testing insert works
        """
        bst = BinarySearchTree()
        key_values = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]

        for i in key_values:
            bst.insert(i, i)

        self.assertEqual(bst.root.value, 3)
        self.assertEqual(bst.root.right.value, 8)
        self.assertEqual(bst.root.right.right.value, 9)
        self.assertEqual(bst.root.right.left.value, 5)
        self.assertEqual(bst.root.right.left.right.right.value, 7)
        self.assertEqual(bst.root.right.left.left.value, 4)
        self.assertEqual(bst.root.right.left.right.value, 6)
        self.assertEqual(bst.root.left.value, 1)
        self.assertEqual(bst.root.left.left.value, 0)
        self.assertEqual(bst.root.left.right.value, 2)

    def test_insert_works_fine(self):
        """
        testing insert works
        """
        bst = BinarySearchTree()
        key_values = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]

        for i in key_values:
            bst.insert(i, i)

        bst.insert(3, "ny")

        self.assertEqual(bst.root.value, "ny")

    def test_is_bst(self):
        """
        bst is correctly implemented
        """
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)
        key_values = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]

        for i in key_values:
            bst.insert(i, i)

        self.assertTrue(self.is_bst(bst.root))

    def is_bst(self, node, lower=float('-inf'), upper=float('inf')):
        """
        check that it is a bst
        """
        if not node:
            return True
        if not lower < node.key < upper:
            return False
        return self.is_bst(node.left, lower, node.key) and self.is_bst(node.right, node.key, upper)


if __name__ == '__main__':
    unittest.main()
