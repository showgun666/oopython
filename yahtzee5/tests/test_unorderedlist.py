#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class unorderedList """
import unittest
from src.unorderedList import UnorderedList
from src.errors import MissingIndex
from src.errors import MissingValue

class TestUnorderedlist(unittest.TestCase):
    """
    Submodule for unittests, derives from unittest.TestCase
    """

    def test_init(self):
        """
        List is initialized correctly
        """
        # Arrange
        uol = UnorderedList()
        # Assert
        self.assertEqual(uol.get_head().next, None)

    def test_append_empty_unordered_list(self):
        """
        Can append to empty list
        """

        # Arrange
        uol = UnorderedList()
        # Act
        uol.append(0)
        # Assert
        self.assertNotEqual(uol.get_head(), None)
        self.assertEqual(uol.get_head().next.data, 0)
        self.assertEqual(uol.get_head().next.next, None)

    def test_append_multiple_values(self):
        """
        Can append multiple values to list
        """
        # Arrange
        uol = UnorderedList()
        # Act
        uol.append(0)
        uol.append(1)
        uol.append(2)
        # Assert
        self.assertNotEqual(uol.get_head(), None)
        self.assertEqual(uol.get_head().next.data, 0)
        self.assertEqual(uol.get_head().next.next.data, 1)
        self.assertEqual(uol.get_head().next.next.next.data, 2)
        self.assertEqual(uol.get_head().next.next.next.next, None)

    def test_set_empty_list(self):
        """
        cannot set value to empty list
        """
        # Arrange
        uol = UnorderedList()
        # Assert
        with self.assertRaises(MissingIndex):
            uol.set(-1, 1)
        with self.assertRaises(MissingIndex):
            uol.set(0, 1)
        with self.assertRaises(MissingIndex):
            uol.set(1, 1)

    def test_set_index(self):
        """
        can set value of an index
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        uol.append(1)
        uol.append(2)
        uol.append(3)
        # Act
        uol.set(0, "a")
        uol.set(1, "b")
        uol.set(2, "c")
        uol.set(3, "d")
        # Assert
        self.assertEqual(uol.get_head().next.data, "a")
        self.assertEqual(uol.get_head().next.next.data, "b")
        self.assertEqual(uol.get_head().next.next.next.data, "c")
        self.assertEqual(uol.get_head().next.next.next.next.data, "d")

    def test_set_index_out_of_range(self):
        """
        setting index out of range raises an exception
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        # Act & Assert
        with self.assertRaises(MissingIndex):
            uol.set(5, 4)

    def test_size_of_empty_list(self):
        """
        Size of empty list returns 0
        """
        # Arrange
        uol = UnorderedList()
        # Assert
        self.assertEqual(uol.size(), 0)

    def test_size_returns_correct_length(self):
        """
        Size returns correct length
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        uol.append(1)
        uol.append(2)
        uol.append(3)

        # Assert
        self.assertEqual(uol.size(), 4)

    def test_get_empty_list(self):
        """
        Get raises exception on empty list
        """
        # Arrange
        uol = UnorderedList()
        # Assert
        with self.assertRaises(MissingIndex):
            uol.get(0)
            uol.get(1)

    def test_get_value_out_of_range(self):
        """
        Get raises exception when out of range
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        uol.append(1)
        uol.append(2)
        uol.append(3)
        # Assert
        with self.assertRaises(MissingIndex):
            uol.get(5)

    def test_get_value_from_index(self):
        """
        Get returns correct value
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        uol.append(1)
        uol.append(2)
        uol.append(3)
        # Assert
        self.assertEqual(uol.get(0), 0)
        self.assertEqual(uol.get(1), 1)
        self.assertEqual(uol.get(2), 2)
        self.assertEqual(uol.get(3), 3)
        self.assertNotEqual(uol.get(3), 2)

    def test_index_of_without_value_raises_exception(self):
        """
        index_of on list without value raises exception
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        uol.append(5)
        uol.append(2)
        uol.append(3)
        # Assert
        with self.assertRaises(MissingValue):
            uol.index_of(1)
            uol.index_of(4)

    def test_index_of_returns_correct_index(self):
        """
        index_of returns correct index
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        uol.append(5)
        uol.append(2)
        uol.append(3)
        # Assert
        self.assertEqual(uol.index_of(0), 0)
        self.assertEqual(uol.index_of(5), 1)
        self.assertEqual(uol.index_of(2), 2)
        self.assertEqual(uol.index_of(3), 3)

    def test_remove(self):
        """
        Remove removes specified item from list
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        uol.append(5)
        uol.append(2)
        uol.append(3)
        # Act
        uol.remove(5)
        # Assert
        self.assertNotEqual(uol.get(1), 5)
        self.assertEqual(uol.get(2), 3)

    def test_remove_raises_exception_on_missing_item(self):
        """
        Remove raises exception when an item is missing
        """
        # Arrange
        uol = UnorderedList()
        uol.append(0)
        uol.append(5)
        uol.append(2)
        uol.append(3)
        with self.assertRaises(MissingValue):
            uol.remove(4)

    def test_print_list(self):
        """
        print_list properly prints contents
        """
        # Arrange
        uol = UnorderedList()
        uol.append("one")
        uol.append("two")
        uol.append("three")
        uol.append("four")

        self.assertIn("one", uol.print_list())
        self.assertIn("four", uol.print_list())
