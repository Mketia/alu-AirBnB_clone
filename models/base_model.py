#!/usr/bin/python3
"""script for the base model"""

import uuid
from models import storage
from datetime import datetime

class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self,*args, **kwargs):
        """Initializes the BaseModel with instance attributes

        Args:
        *args: list of arguments
        **kwargs: dict of key-values arguments
        """
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"]= datetime.strptime(
                        kwargs["created_at"],"%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_att":
                    self.__dict__["updated_at"]= datetime.strptime(
                        kwargs["updated_at"],"%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key]=kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Updates the attribute `updated_at` with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict= self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict