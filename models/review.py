#!/usr/bin/python3
"""Module to create a review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """class dedicated to review objects"""
    place_id = ""
    User_id = ""
    text = ""