#!/usr/bin/python3
"""Unittest for the user class"""

import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.user = User()

    def test_inherits_baseModel(self):
        """Test if user inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_fname(self):
        """Test if attributes are set correctly"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")

    def test_email(self):
        """Test if attributes are set correctly"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")

    def test_password(self):
        """Test if attributes are set correctly"""
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

    def test_lname(self):
        """Test if attributes are set correctly"""
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")
    
    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.user.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_str(self):
        """ test ___str___ method """
        correct = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(correct, str(self.user))


if __name__ == "__main__":
    unittest.main()
