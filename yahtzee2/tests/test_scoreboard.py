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

    def test_get_points_from_rule(self):
        rules = {
            "Ones": 3,
            "Twos": 4,
            "Threes": 9,
            "Fours": 12,
            "Fives": 25,
            "Sixes": 12,
            "Three Of A Kind": 11,
            "Four Of A Kind": 14,
            "Full House": -1,
            "Small Straight": -1,
            "Large Straight": 40,
            "Yahtzee": -1,
            "Chance": -1,
            }
        my_scoreboard = Scoreboard.from_dict(rules)

        assert(my_scoreboard.get_points("Ones") == 3)
        assert(my_scoreboard.get_points("Threes") == 9)
        assert(my_scoreboard.get_points("Large Straight") == 40)
        assert(my_scoreboard.get_points("Small Straight") == -1)
        assert(my_scoreboard.get_points("Sixes") == 12)
