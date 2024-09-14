#!/usr/bin/python3
"""Unittest for the Place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.place = Place()

    def test_inherits_baseModel(self):
        """Test if Place inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_city_id(self):
        """Test city_id attribute"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """Test user_id attribute"""
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """Test name attribute"""
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """Test description attribute"""
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """Test number_rooms attribute"""
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test number_bathrooms attribute"""
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """Test max_guest attribute"""
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """Test price_by_night attribute"""
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """Test latitude attribute"""
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """Test longitude attribute"""
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """Test amenity_ids attribute"""
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict(self):
        """Test to_dict() method"""
        place_dict = self.place.to_dict()
        self.assertEqual(type(place_dict), dict)
        

if __name__ == "__main__":
    unittest.main()
