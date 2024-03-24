#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the class Leaderboard """
import unittest
from src.leaderboard import Leaderboard

class TestLeaderboard(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def test_add_entry_to_leaderboard(self):
        """ Entries can be added to leaderboard """
        lb = Leaderboard()
        harry = ("Harry", 300)
        hermione = ("Hermione", 500)
        ron = ("Ron", 250)
        lb.add_entry(harry[0], harry[1])
        lb.add_entry(hermione[0], hermione[1])
        lb.add_entry(ron[0], ron[1])

        self.assertEqual(lb.entries.size(), 3)
        self.assertEqual(lb.entries.get(0), harry)
        self.assertEqual(lb.entries.get(1), hermione)
        self.assertEqual(lb.entries.get(2), ron)

    def test_remove_entry_from_leaderboard(self):
        """ Entries can be removed from leaderboard """
        lb = Leaderboard()
        harry = ("Harry", 300)
        hermione = ("Hermione", 500)
        ron = ("Ron", 250)
        lb.add_entry(harry[0], harry[1])
        lb.add_entry(hermione[0], hermione[1])
        lb.add_entry(ron[0], ron[1])

        lb.remove_entry(1)

        self.assertEqual(lb.entries.size(), 2)
        self.assertEqual(lb.entries.get(0), harry)
        self.assertEqual(lb.entries.get(1), ron)

    def test_save_data_to_file(self):
        """ Entries can be saved to a file """
        lb = Leaderboard()
        harry = ("300", "Harry")
        hermione = (500, "Hermione")
        ron = ("250", "Ron")
        lb.add_entry(harry[0], harry[1])
        lb.add_entry(hermione[0], hermione[1])
        lb.add_entry(ron[0], ron[1])

        lb.save("test.txt")
        lines = []
        with open("test.txt", "r", encoding="utf-8") as f:
            for line in f:
                lines.append(line)
        self.assertEqual("300;Harry\n", lines[0])

    def test_dunder_string(self):
        """ Entries can be printed with dunder method """
        lb = Leaderboard()
        harry = ("Harry", 200)
        hermione = ("Hermione", 400)
        lb.add_entry(harry[0], harry[1])
        lb.add_entry(hermione[0], hermione[1])

        self.assertIn("Harry", str(lb))
        self.assertIn("Hermione", str(lb))
        self.assertIn("200", str(lb))

    def test_load_file(self):
        """ Leaderboard object can be created from file """
        lb = Leaderboard.load("test.txt")

        self.assertTrue(lb[1])
        self.assertEqual(lb[2], ('250', 'Ron'))

    def test_while_loop(self):
        """ Leaderboard can be iterated over with while """
        lb = Leaderboard()

        harry = ("Harry", "300")
        hermione = ("Hermione", 500)
        ron = ("Ron", "250")
        lb.add_entry(harry[0], harry[1])
        lb.add_entry(hermione[0], hermione[1])
        lb.add_entry(ron[0], ron[1])

        entries = []
        boardlength = len(lb)

        i = 0
        while i < boardlength:
            entries.append(lb[i])
            i += 1

        self.assertTrue(entries[0])
        self.assertEqual(boardlength, 3)
        self.assertEqual(entries[0], ("Harry", "300"))
        self.assertEqual(entries[2], ("Ron", "250"))
