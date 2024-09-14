#!/usr/bin/python3
"""Unittest for the City class"""

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up an instance for testing"""
        self.city = City()

    def tearDown(self):
        """Clean up after each test"""
        del self.city

    def test_inherits_baseModel(self):
        """Test if City class inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes_exist(self):
        """Test if City has the correct attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_default_values(self):
        """Test default values of attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_save(self):
        """Test if save() updates the `updated_at` attribute"""
        old_updated_at = self.city.updated_at
        sleep(0.1)  # Sleep for a short time to ensure updated_at changes
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_to_dict(self):
        """Test to_dict() method creates a correct dictionary"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs from to_dict"""
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertEqual(self.city.id, new_city.id)
        self.assertEqual(self.city.created_at, new_city.created_at)
        self.assertEqual(self.city.updated_at, new_city.updated_at)
        self.assertEqual(self.city.state_id, new_city.state_id)
        self.assertEqual(self.city.name, new_city.name)

if __name__ == "__main__":
    unittest.main()
