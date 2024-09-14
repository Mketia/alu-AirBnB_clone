#!/usr/bin/python3
""" Module for testing the BaseModel class """
import unittest
import time
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel class """

    def setUp(self):
        """ Set up test environment """
        self.model = BaseModel()

    def tearDown(self):
        """ Clean up test environment """
        del self.model
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_instance(self):
        """ Test if the object is an instance of BaseModel """
        self.assertIsInstance(self.model, BaseModel)

    def test_id_is_string(self):
        """ Test if id is a string after initialization """
        self.assertIsInstance(self.model.id, str)

    def test_unique_ids(self):
        """ Test if two BaseModel instances have unique ids """
        another_model = BaseModel()
        self.assertNotEqual(self.model.id, another_model.id)

    def test_created_at(self):
        """ Test if created_at is a datetime object """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """ Test if updated_at is a datetime object """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """ Test if save() updates the `updated_at` attribute """
        old_updated_at = self.model.updated_at
        time.sleep(0.01)
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """ Test if to_dict() creates a dictionary with correct attributes """
        model_dict = self.model.to_dict()
        self.assertEqual(self.model.id, model_dict['id'])
        self.assertEqual(self.model.created_at.isoformat(), model_dict['created_at'])
        self.assertEqual(self.model.updated_at.isoformat(), model_dict['updated_at'])
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_to_dict_type(self):
        """ Test if to_dict() returns a dictionary """
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_str_method(self):
        """ Test if the __str__ method has the correct output """
        model_str = str(self.model)
        expected_output = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(model_str, expected_output)

    def test_kwargs_instantiation(self):
        """ Test instantiation with kwargs """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)

    def test_save_creates_file(self):
        """ Test that save() creates a file named 'file.json' """
        self.model.save()
        self.assertTrue(os.path.exists('file.json'))


if __name__ == '__main__':
    unittest.main()
