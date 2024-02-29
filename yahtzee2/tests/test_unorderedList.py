#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class unorderedList """
import unittest
from src.unorderedList import UnorderedList

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
