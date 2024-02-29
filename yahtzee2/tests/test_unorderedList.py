#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class unorderedList """
import unittest
from src.unorderedList import UnorderedList
from src.errors import MissingIndex
from src.errors import MissingValue

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

    def testSizeOfEmptyList(self):
        """
        Size of empty list returns 0
        """
        # Arrange
        unorderedList = UnorderedList()
        # Assert
        self.assertEqual(unorderedList.size(), 0)

    def testSizeReturnsCorrectLength(self):
        """
        Size returns correct length
        """
        # Arrange
        unorderedList = UnorderedList()
        unorderedList.append(0)
        unorderedList.append(1)
        unorderedList.append(2)
        unorderedList.append(3)

        # Assert
        self.assertEqual(unorderedList.size(), 4)

    def testGetEmptyList(self):
        """
        Get on empty list raises an exception
        """
        # Arrange
        unorderedList = UnorderedList()
        # Assert
        with self.assertRaises(MissingIndex):
            unorderedList.get(0)
            unorderedList.get(1)

    def testGetValueOutOfRange(self):
        """
        Get on empty list raises an exception
        """
        # Arrange
        unorderedList = UnorderedList()
        unorderedList.append(0)
        unorderedList.append(1)
        unorderedList.append(2)
        unorderedList.append(3)
        # Assert
        with self.assertRaises(MissingIndex):
            unorderedList.get(5)

    def testGetValueFromIndex(self):
        """
        Get returns correct value
        """
        # Arrange
        unorderedList = UnorderedList()
        unorderedList.append(0)
        unorderedList.append(1)
        unorderedList.append(2)
        unorderedList.append(3)
        # Assert
        self.assertEqual(unorderedList.get(0), 0)
        self.assertEqual(unorderedList.get(1), 1)
        self.assertEqual(unorderedList.get(2), 2)
        self.assertEqual(unorderedList.get(3), 3)
        self.assertNotEqual(unorderedList.get(3), 2)

    def testIndexOfWithoutValueRaisesException(self):
        """
        index_of on list without value raises exception
        """
        # Arrange
        unorderedList = UnorderedList()
        unorderedList.append(0)
        unorderedList.append(5)
        unorderedList.append(2)
        unorderedList.append(3)
        # Assert
        with self.assertRaises(MissingValue):
            unorderedList.index_of(1)
            unorderedList.index_of(4)

    def testIndexOfReturnsCorrectIndex(self):
        """
        index_of returns correct index
        """
        # Arrange
        unorderedList = UnorderedList()
        unorderedList.append(0)
        unorderedList.append(5)
        unorderedList.append(2)
        unorderedList.append(3)
        # Assert
        self.assertEqual(unorderedList.index_of(0), 0)
        self.assertEqual(unorderedList.index_of(5), 1)
        self.assertEqual(unorderedList.index_of(2), 2)
        self.assertEqual(unorderedList.index_of(3), 3)

    def testRemove(self):
        """
        Remove removes specified item from list
        """
        # Arrange
        unorderedList = UnorderedList()
        unorderedList.append(0)
        unorderedList.append(5)
        unorderedList.append(2)
        unorderedList.append(3)
        # Act
        unorderedList.remove(5)
        # Assert
        self.assertNotEqual(unorderedList.get(1), 5)
        self.assertEqual(unorderedList.get(2), 3)
