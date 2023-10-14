#!usr/bin/python3
"""File Storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """File Storage Class

    Attributes:
        __file_path (str): file path to save objects
        __objects (dict): dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict of all objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets an object in the __objects dict"""
        key = obj.__class_.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        _dict = FileStorage.__objects
        data = {obj: _dict[obj].to_dict() for obj in _dict.keys()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as File:
            json.dump(data, File)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as File:
                data = json.load(File)
                for key, value in data.items():
                    class_name, obj_id = key_split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
