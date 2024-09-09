#!/usr/bin/python3
"""Module to create a user class"""

from models.base_model import BaseModel

class User(BaseModel):
    """class dedicated to user objects"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""