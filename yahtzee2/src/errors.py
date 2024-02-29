"""
Module for custom exceptions
"""
class Error(Exception):
   """User defined class for custom exceptions"""

class MissingIndex(Error):
   """Raised when an index is not found"""

class MissingValue(Error):
   """Raised when a value is not found"""
