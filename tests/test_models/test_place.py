#!/usr/bin/python3
"""Unittest for the state class"""

import unittest
from models.city import City
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.city = City()

    def test_inherits_baseModel(self):
        """Test if user inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_stateid(self):
        """ test state_id """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")

    def testname(self):
        """ test name """
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")
    

if __name__ == "__main__":
    unittest.main()
