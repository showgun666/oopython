#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class Die """
import unittest
import random
from src.die import Die
from src.hand import Hand
from src.rule import Rule, SameValueRule, Ones, ThreeOfAKind, FourOfAKind, FullHouse, SmallStraight

class TestDie(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Setup that runs before every testcase """
        random.seed("rule")

    def test_ones(self):
        """ Count ones in a hand. """
        my_hand = Hand([1,2,2,2,2])
        my_rule = Ones()
        points = my_rule.points(my_hand)
        self.assertEqual(points, 1) # Assert

    def test_three_of_a_kind(self):
        """ Make sure ThreeOfAkind returns the correct value. """
        my_hand = Hand([4,5,3,5,6])
        my_rule = ThreeOfAKind()
        points = my_rule.points(my_hand)
        self.assertEqual(points, None) # Assert 1
        my_hand = Hand([6,5,6,6,2])
        points = my_rule.points(my_hand)
        self.assertEqual(points, 25) # Assert 2

    def test_four_of_a_kind(self):
        """ Make sure FourOfAkind returns the correct value. """
        my_hand = Hand([1,1,1,1,6])
        my_rule = FourOfAKind()
        my_hand.dice[4]._value = 6
        points = my_rule.points(my_hand) # 1 1 1 1 6
        self.assertEqual(points, 10) # Assert 1 10

        my_hand.roll()
        points = my_rule.points(my_hand)
        self.assertEqual(points, None) # Assert 2 None
    
    def test_full_house(self):
        """ Make sure FullHouse returns the correct value. """
        my_hand = Hand([1,1,1,6,6])
        my_rule = FullHouse()
        points = my_rule.points(my_hand)
        self.assertEqual(points, 25) # Assert 1 25

        my_hand.roll()
        points = my_rule.points(my_hand)
        self.assertEqual(points, None) # Assert 2 None

    def test_small_straight(self):
        """ Test Small Straight for functionality. """
        my_hand = Hand([1,1,2,3,4])
        my_rule = SmallStraight()
        points = my_rule.points(my_hand)
        self.assertEqual(points, 30) # Assert Low

        my_hand = Hand([1,2,3,5,6])
        points = my_rule.points(my_hand)
        self.assertEqual(points, None) # Assert None
        
        my_hand = Hand([6,3,2,4,1])
        points = my_rule.points(my_hand)
        self.assertEqual(points, 30) # Assert Scramble

        my_hand = Hand([2,5,2,3,4])
        points = my_rule.points(my_hand)
        self.assertEqual(points, 30) # Assert Middle

        my_hand = Hand([6,5,5,3,4])
        points = my_rule.points(my_hand)
        self.assertEqual(points, 30) # Assert High

        my_hand = Hand([4,2,3,5,6])
        points = my_rule.points(my_hand)
        self.assertEqual(points, 30) # Assert 5 straight