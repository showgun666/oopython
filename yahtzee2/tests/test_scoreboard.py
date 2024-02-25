#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class Scoreboard """
import unittest
import random
from src.scoreboard import Scoreboard
from src.hand import Hand

class TestScoreboard(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Setup that runs before every testcase """
        random.seed("scoreboard")

    def test_add_points_rule(self):
        """ Test adding points for a rule. """
        my_scoreboard = Scoreboard() # Arrange
        my_hand = Hand([5,1,2,3,1])

        my_scoreboard.add_points("Ones", my_hand) # Act
        my_scoreboard.add_points("Threes", my_hand)

        self.assertEqual(my_scoreboard.get_points("Ones"), 2) # Assert
        self.assertEqual(my_scoreboard.get_points("Threes"), 3)

    def test_add_points_to_rule_with_points(self):
        """ Test adding points for a rule that already has points. """
        my_scoreboard = Scoreboard()
        my_hand = Hand([5,1,2,3,1])

        my_scoreboard.add_points("Ones", my_hand)
        with self.assertRaises(ValueError) as _:
            my_scoreboard.add_points("Ones", my_hand)
