"module for custom exceptions for Trie class"

class Error(Exception):
    """User defined class for custom exceptions"""

class SearchMiss(Error):
    """Raised when a word is not found in trie"""
