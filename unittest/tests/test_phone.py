import unittest
from src.phone import Phone

class TestPhone(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        # Arrange
        self.phone = Phone("Samsung", "Galaxy S8", "Android")

    def tearDown(self):
        """ Remove dependencies after test """
        self.phone = None

    def test_default_owner(self):
        """Test that default value if correct for owner"""
        # Assert
        self.assertEqual(self.phone.owner, "No owner yet")

    def test_init(self):
        """Test that init works as expected"""
        # Assert
        self.assertEqual(self.phone.owner, "No owner yet")
        self.assertEqual(self.phone.manufacturer, "Samsung")
        self.assertEqual(self.phone.model, "Galaxy S8")
        self.assertEqual(self.phone.os, "Android")
        self.assertEqual(self.phone._phonebook, [])

    def test_empty_phonebook(self):
        """Test that has_contacts return False when phonebook is empty"""
        self.assertFalse(self.phone.has_contacts()) # Assert

    def test_has_contact_true(self):
        """Test that has_contacts return True when phonebook is has a contact"""
        self.phone._phonebook.append("070-354 78 00") # Arrange
        self.assertTrue(self.phone.has_contacts()) # Assert

    def test_validate_valid_number(self):
        """Test validating valid number"""
        self.assertTrue(self.phone.validate_number("070-354 78 00"))

    def test_validate_number_with_letter(self):
        """Test validating number with a letter init"""
        self.assertFalse(self.phone.validate_number("070-35b 78 00"))

    def test_valid_number_with_missing_space(self):
        """Test validating number with a space missing"""
        self.assertFalse(self.phone.validate_number("070-354 7800"))

    def test_get_contact_empty(self):
        """
        Test that error is raised when list is empty
        """
        with self.assertRaises(ValueError) as _:
            self.phone.get_contact("Missing")

    def test_get_contact_fail(self):
        """
        Test that correct value is returned
        when getting contact that does not exist or is empty
        """
        self.phone.add_contact("Andreas", "079-244 07 80")
        with self.assertRaises(ValueError) as _:
            self.phone.get_contact("Zeldah")

    def test_get_contact(self):
        """Test that can get added contact"""
        self.phone.add_contact("Andreas", "079-244 07 80")
        self.assertEqual(self.phone.get_contact("Andreas"), ("Andreas", "079-244 07 80"))
