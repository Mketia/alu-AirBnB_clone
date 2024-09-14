#!/usr/bin/python3
"""Unittest for the Amenity class"""

import unittest
import time
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.amenity = Amenity()

    def test_inherits_baseModel(self):
        """Test if Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_attributes(self):
        """Test if attributes are set correctly"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_save(self):
        """ Test if save() updates the `updated_at` attribute """
        old_updated_at = self.amenity.updated_at
        time.sleep(0.01)
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_str_method(self):
        """ Test if the __str__ method has the correct output """
        model_str = str(self.amenity)
        expected_output = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(model_str, expected_output)

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.amenity.to_dict()
        self.assertEqual(type(new_dict), dict)

if __name__ == "__main__":
    unittest.main()