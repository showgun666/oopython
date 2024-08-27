#!/usr/bin/env python3
#pylint: disable=protected-access
"Test module for Trie class"

import unittest
from src.trie import Trie
from src.exceptions import SearchMiss

class TestTrie(unittest.TestCase):
    "class for testing Trie class"

    def test_add_word(self):
        "word can be added to Trie"
        trie = Trie()

        trie.add_word("cow")
        trie.add_word("cot")
        trie.add_word("cat")
        trie.add_word("BAT") # case sensitivity

        self.assertEqual(trie.root.children["c"].children["o"].children["w"].is_end_of_word, True)
        self.assertEqual(trie.root.children["c"].children["o"].children["t"].is_end_of_word, True)
        self.assertEqual(trie.root.children["c"].children["a"].children["t"].is_end_of_word, True)
        self.assertEqual(trie.root.children["b"].children["a"].children["t"].is_end_of_word, True)
        self.assertEqual(trie.root.children["c"].children["o"].is_end_of_word, False)
        # TEST IF SAME WORD CAN BE ADDED TWICE

    def test_create_from_file(self):
        "Trie can be created from file"
        file = "dictionaries/tiny_dictionary.txt"
        trie = Trie.create_from_file(file)

        self.assertIsInstance(trie, Trie)

    def test_find_word_in_trie(self):
        "Words can be found in trie"
        file = "dictionaries/tiny_dictionary.txt"
        trie = Trie.create_from_file(file)

        self.assertTrue(trie.find_word("term"))
        self.assertTrue(trie.find_word("danced"))
        self.assertTrue(trie.find_word("outfit"))
        self.assertTrue(trie.find_word("annex"))
        self.assertTrue(trie.find_word("ANNEX"))
        self.assertTrue(trie.find_word("OuTfIt"))
        self.assertTrue(trie.find_word("   danced "))
        self.assertFalse(trie.find_word("Billybob"))

    def test_remove_word(self):
        "words can be removed from trie"
        file = "dictionaries/tiny_dictionary.txt"
        trie = Trie.create_from_file(file)

        trie.remove_word("annex")
        trie.remove_word("danced")
        trie.remove_word("outfit")

        self.assertEqual(trie.find_word("annex"), False)
        self.assertEqual(trie.find_word("danced"), False)
        self.assertEqual(trie.find_word("outfit"), False)
        self.assertTrue(trie.find_word("term"))


    def test_remove_word_not_in_trie_raises_exception(self):
        "Trying to remove nonexistent word raises exception"
        file = "dictionaries/tiny_dictionary.txt"
        trie = Trie.create_from_file(file)

        # Not added word
        with self.assertRaises(SearchMiss) as _:
            trie.remove_word("bankautomat")
        # Prefix
        with self.assertRaises(SearchMiss) as _:
            trie.remove_word("ena")
        # Suffix
        with self.assertRaises(SearchMiss) as _:
            trie.remove_word("darned")

    def test_count_words(self):
        "correctly counts words in trie"
        file = "dictionaries/tiny_dictionary.txt"
        trie = Trie.create_from_file(file)
        trie_empty = Trie()

        self.assertEqual(trie.count_words(), 170)
        trie.remove_word("the")
        self.assertEqual(trie.count_words(), 169)
        self.assertEqual(trie_empty.count_words(), 0)

    def test_get_words(self):
        "can get words from trie"
        file = "dictionaries/tiny_dictionary.txt"
        trie = Trie.create_from_file(file)
        trie_empty = Trie()

        trie.add_word("GLASS")
        gotten_words = trie.get_words()
        
        self.assertEqual(trie_empty.get_words(), [])
        self.assertEqual(len(gotten_words), 171)
        self.assertIn("the", gotten_words)
        self.assertIn("annex", gotten_words)
        self.assertIn("glass", gotten_words)
        self.assertNotIn("GLASS", gotten_words)

    def test_prefix_search(self):
        "prefix search works as expected"
        file = "dictionaries/tiny_dictionary.txt"
        trie = Trie.create_from_file(file)

        self.assertIn("the", trie.prefix_search("th"))
        self.assertIn("thermal", trie.prefix_search("TH"))
        self.assertIn("thomas", trie.prefix_search("th"))
        self.assertIn("thomas", trie.prefix_search("   th  "))
        self.assertEqual([], trie.prefix_search("thzq"))
