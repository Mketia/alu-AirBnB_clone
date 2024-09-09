#!/usr/bin/python3
"""Unittest for the state class"""

import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up an instance for testing"""
        self.review = Review()

    def test_inherits_baseModel(self):
        """Test if user inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_placeid(self):
        """ test place_id attribute """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")

    def test_text(self):
        """ test text attribute """
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_user_id(self):
        """ test user_id """
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

    

if __name__ == "__main__":
    unittest.main()
