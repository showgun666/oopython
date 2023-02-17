#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class Die """
import unittest
import random
from src.hand import Hand
from src.die import Die

class TestDie(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Setup that runs before every testcase """
        random.seed("hand")

    def test_to_list(self):
        """ Attempts to create a list from a hand. """
        my_hand = Hand([5,1,2,3,1])
        my_list = my_hand.to_list() # Act
        
        # Asserts x5
        self.assertEqual(my_list[0], 5) # Pos 1 is 5
        self.assertEqual(my_list[1], 1) # Pos 2 is 1
        self.assertEqual(my_list[2], 2) # Pos 3 is 2
        self.assertEqual(my_list[3], 3) # Pos 4 is 3
        self.assertEqual(my_list[4], 1) # Pos 5 is 4
