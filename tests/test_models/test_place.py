#!/usr/bin/python3
"""Unittest for the state class"""

import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.place = Place()

    def test_inherits_baseModel(self):
        """Test if user inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_city_id(self):
        """ test city_id """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """ test user_id """
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """ test name """
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """ test description """
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """ test number_rooms """
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """ test number_bathrooms """
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """ test max_guest """
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """ test price_by_night """
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """ test latitude """
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """ test longitude """
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """ test amenity_ids """
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])
    

if __name__ == "__main__":
    unittest.main()
