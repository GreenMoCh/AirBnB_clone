#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents city

    Attributes:
        state_id (str): state id
        name (str): city name
    """

    state_id = ""
    name = ""
