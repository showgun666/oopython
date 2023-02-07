#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class Die """
import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Setup that runs before every testcase """
        random.seed("die")

    def test_create_without_argument(self):
        """ Attempt to create a die without an argument. """
        my_die = Die() # Act
        self.assertIsNotNone(my_die.get_value()) # Assert

    def test_create_with_argument(self):
        """ Attempt to create a die with an argument. """
        my_die = Die(5) # Act
        self.assertEqual(my_die.get_value(), 5) # Assert

    def test_create_with_wrong_argument(self):
        """ Attempt to create a die with an argument outside of allowed range. """
        my_die1 = Die(100) # Act1
        self.assertIsNot(my_die1.get_value(), 100) # Assert 1

        my_die2 = Die(0) # Act2
        self.assertIsNot(my_die2.get_value(), 0) # Assert 2

    def test_roll_sets_new_value(self):
        """ Check if roll method sets a new value for die. """
        my_die = Die()
        my_die.roll() # 5 Act 1
        self.assertEqual(my_die.get_value(), 5) # Assert 1
        my_die.roll() # 4 Act 2
        self.assertEqual(my_die.get_value(), 4) # Assert 2
        my_die.roll() # 3 Act 3
        self.assertEqual(my_die.get_value(), 3) # Assert 3
        my_die.roll() # 3 Act 4
        self.assertEqual(my_die.get_value(), 3) # Assert 4
        my_die.roll() # 4 Act 5
        self.assertEqual(my_die.get_value(), 4) # Assert 5

    def test_get_name_returns_correct_name(self):
        """ Check if get_name returns correct name. """
        my_die = Die() # Act
        # Assert block
        if my_die.get_value() == 1:
            self.assertEqual(my_die.get_name(), "one")
        elif my_die.get_value() == 2:
            self.assertEqual(my_die.get_name(), "two")
        elif my_die.get_value() == 3:
            self.assertEqual(my_die.get_name(), "three")
        elif my_die.get_value() == 4:
            self.assertEqual(my_die.get_name(), "four")
        elif my_die.get_value() == 5:
            self.assertEqual(my_die.get_name(), "five")
        else:
            self.assertEqual(my_die.get_name(), "six")

    def test_string_functionality(self):
        """ Check if __str__() returns correct value as a string. """
        my_die = Die()
        self.assertEqual(int(str(my_die)), my_die._value) # Assert
