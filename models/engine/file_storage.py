#!/usr/bin/python3
"""module for serialization and deserialization of BaseModel instances """

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review
import os

class FileStorage:
    """class for serializing or deserializing a json file"""

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of valid classes"""
        return{
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
        obj: The object to store
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key]= obj
    
    def save(self):
        """Serializes __objects to the JSON file."""
        newdict = {}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for k, v in self.__objects.items():
                newdict[k] = v.to_dict()
            json.dump(newdict, f)

    def reload(self):
        """Deserializes the JSON file if the file exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    self.__objects[k] = self.classes()[v["__class__"]](**v)



