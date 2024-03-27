#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the sort module """
import unittest
from src.sort import insertion_sort, recursive_insertion
from src.unordered_list import UnorderedList

class TestSort(unittest.TestCase):
    """
    Submodule for unittests, derives from unittest.TestCase
    """

    def test_insertion_sort(self):
        """
        insertion_sort accurately sorts unordered list
        """
        uol = UnorderedList()
        uol.append(1)
        uol.append(6)
        uol.append(3)
        uol.append(8)
        uol.append(2)

        sorted_list = insertion_sort(uol)

        self.assertEqual(sorted_list.get(0), 1)
        self.assertEqual(sorted_list.get(1), 2)
        self.assertEqual(sorted_list.get(2), 3)
        self.assertEqual(sorted_list.get(3), 6)
        self.assertEqual(sorted_list.get(4), 8)

    def test_recursive_insertion_integers(self):
        """
        recursive_insertion accurately sorts unordered list
        """
        uol = UnorderedList()
        uol.append(1)
        uol.append(33)
        uol.append(6)
        uol.append(3)
        uol.append(15)
        uol.append(8)
        uol.append(2)
        uol.append(11)

        sorted_list = recursive_insertion(uol, 1)

        self.assertEqual(sorted_list.get(0), 1)
        self.assertEqual(sorted_list.get(1), 2)
        self.assertEqual(sorted_list.get(2), 3)
        self.assertEqual(sorted_list.get(3), 6)
        self.assertEqual(sorted_list.get(4), 8)
        self.assertEqual(sorted_list.get(5), 11)
        self.assertEqual(sorted_list.get(6), 15)
        self.assertEqual(sorted_list.get(7), 33)

    def test_recursive_insertion_strings(self):
        """
        recursive_insertion sorts strings
        """
        uol = UnorderedList()
        uol.append("ab")
        uol.append("33")
        uol.append("_2345e")
        uol.append("IVARS")
        uol.append("DUBBelDATA")
        uol.append("Toffel")
        uol.append("Fjorton")
        uol.append("Dbwebb")
        uol.append("dbwebb")

        sorted_list = recursive_insertion(uol, 1)

        self.assertEqual(sorted_list.get(0), "33")
        self.assertEqual(sorted_list.get(1), "DUBBelDATA")
        self.assertEqual(sorted_list.get(2), "Dbwebb")
        self.assertEqual(sorted_list.get(3), "Fjorton")
        self.assertEqual(sorted_list.get(4), "IVARS")
        self.assertEqual(sorted_list.get(5), "Toffel")
        self.assertEqual(sorted_list.get(6), "_2345e")
        self.assertEqual(sorted_list.get(7), "ab")
        self.assertEqual(sorted_list.get(8), "dbwebb")

    def test_recursive_insertion_tuple(self):
        """
        recursive_insertion sorts strings and integers
        """
        uol = UnorderedList()
        uol.append(("ab", "2034"))
        uol.append(("abba", "1235"))
        uol.append(("babba", "86234"))
        uol.append(("bub", "123"))
        uol.append(("bab", "425"))
        uol.append(("eb", "1325"))

        sorted_list = recursive_insertion(uol, 1)

        self.assertEqual(sorted_list.get(0)[0], "ab")
        self.assertEqual(sorted_list.get(1)[0], "abba")
        self.assertEqual(sorted_list.get(2)[0], "bab")
        self.assertEqual(sorted_list.get(3)[0], "babba")
        self.assertEqual(sorted_list.get(4)[0], "bub")
        self.assertEqual(sorted_list.get(5)[0], "eb")

    def test_recursive_insertion_reverse(self):
        """
        recursive_insertion accurately sorts unordered list
        """
        uol = UnorderedList()
        uol.append(1)
        uol.append(33)
        uol.append(6)
        uol.append(3)

        sorted_list = recursive_insertion(uol, 1, True)

        self.assertEqual(sorted_list.get(0), 33)
        self.assertEqual(sorted_list.get(1), 6)
        self.assertEqual(sorted_list.get(2), 3)
        self.assertEqual(sorted_list.get(3), 1)

    def test_recursive_insertion_empty_list(self):
        """
        recursive_insertion returns None if given list is empty
        """
        uol = UnorderedList()
        new_list = recursive_insertion(uol, 1)

        self.assertEqual(new_list.size(), 0)

    def test_recursive_insertion_one_index_list(self):
        """
        recursive_insertion can sort a list with one index
        """
        uol = UnorderedList()
        uol.append(1)
        new_list = recursive_insertion(uol, 1)

        self.assertEqual(new_list[0], 1)
