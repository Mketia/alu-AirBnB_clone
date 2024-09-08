#!/usr/bin/python3
"""module for the city class"""

from models.base_model import BaseModel

class City(BaseModel):
    """class dedicated to city objects"""
    state_id = ""
    name = ""