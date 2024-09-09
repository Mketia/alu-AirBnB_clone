#!/usr/bin/python3
"""Unittest for the Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.amenity = Amenity()  # Instantiate the Amenity class

    def test_inherits_baseModel(self):
        """Test if Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test if attributes are set correctly"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

if __name__ == "__main__":
    unittest.main()
