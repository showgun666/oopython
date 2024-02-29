#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class unorderedList """
import unittest
from src.unorderedList import UnorderedList
from src.errors import MissingIndex

class TestUnorderedList(unittest.TestCase):
    """
    Submodule for unittests, derives from unittest.TestCase
    """

    def testInit(self):
        """
        List is initialized correctly
        """
        # Arrange
        unorderedList = UnorderedList()
        # Assert
        self.assertEqual(unorderedList.head.next, None)

    def testAppendEmptyUnorderedList(self):
        """
        Can append to empty list
        """

        # Arrange
        unorderedList = UnorderedList()
        # Act
        unorderedList.append(0)
        # Assert
        self.assertNotEqual(unorderedList.head, None)
        self.assertEqual(unorderedList.head.next.data, 0)
        self.assertEqual(unorderedList.head.next.next, None)

    def testAppendMultipleValues(self):
        """
        Can append multiple values to list
        """
        # Arrange
        unorderedList = UnorderedList()
        # Act
        unorderedList.append(0)
        unorderedList.append(1)
        unorderedList.append(2)
        # Assert
        self.assertNotEqual(unorderedList.head, None)
        self.assertEqual(unorderedList.head.next.data, 0)
        self.assertEqual(unorderedList.head.next.next.data, 1)
        self.assertEqual(unorderedList.head.next.next.next.data, 2)
        self.assertEqual(unorderedList.head.next.next.next.next, None)

    def testSetEmptyList(self):
        """
        cannot set value to empty list
        """
        # Arrange
        unorderedList = UnorderedList()
        # Assert
        with self.assertRaises(MissingIndex):
            unorderedList.set(-1, 1)
        with self.assertRaises(MissingIndex):
            unorderedList.set(0, 1)
        with self.assertRaises(MissingIndex):
            unorderedList.set(1, 1)

    def testSetIndex(self):
        """
        can set value of an index
        """
        # Arrange
        unorderedList = UnorderedList()
        unorderedList.append(0)
        unorderedList.append(1)
        unorderedList.append(2)
        unorderedList.append(3)
        # Act
        unorderedList.set(0, "a")
        unorderedList.set(1, "b")
        unorderedList.set(2, "c")
        unorderedList.set(3, "d")
        # Assert
        self.assertEqual(unorderedList.head.next.data, "a")
        self.assertEqual(unorderedList.head.next.next.data, "b")
        self.assertEqual(unorderedList.head.next.next.next.data, "c")
        self.assertEqual(unorderedList.head.next.next.next.next.data, "d")

    def testSetIndexOutOfRange(self):
        """
        setting index out of range raises an exception
        """
        # Arrange
        unorderedList = UnorderedList()
        unorderedList.append(0)
        # Act & Assert
        with self.assertRaises(MissingIndex):
            unorderedList.set(5, 4)
