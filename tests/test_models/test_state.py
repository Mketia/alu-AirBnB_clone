#!/usr/bin/python3
"""Unittest for the state class"""

import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.state = State()

    def test_inherits_baseModel(self):
        """Test if user inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_name(self):
        """ test name """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

if __name__ == "__main__":
    unittest.main()
