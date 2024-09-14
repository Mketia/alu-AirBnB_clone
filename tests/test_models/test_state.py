#!/usr/bin/python3
"""Unittest for the state class"""

import unittest
from models.state import State
import datetime
import time
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.state = State()

    def test_inherits_baseModel(self):
        """Test if user inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_save(self):
        """ Test if save() updates the `updated_at` attribute """
        old_updated_at = self.state.updated_at
        time.sleep(0.01)
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)


    def test_name(self):
        """ test name """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")
    
    def test_str_method(self):
        """ Test if the __str__ method has the correct output """
        model_str = str(self.state)
        expected_output = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(model_str, expected_output)

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.state.to_dict()
        self.assertEqual(type(new_dict), dict)

if __name__ == "__main__":
    unittest.main()
