#!/usr/bin/python3
"""Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents place

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): place name
        description (str): place description
        number_rooms (int) : rooms num
        number_bathroom (int): bath num
        max_guest (int): max of gests num
        price_by_night (int): price by night of the place
        latitude (float): laltidude of place
        longitude (float): longitude of the place
        amenity_ids (list): list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price by night = 0
    latidude = 0.0
    longitude = 0.0
    amenity_ids = []
