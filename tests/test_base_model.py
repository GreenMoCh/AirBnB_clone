#!/usr/bin/python3
"""BaseModel Unittest"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """BaseModel test cases"""

    def test_attributes(self):
        """Atrributes test"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_id_generation(self):
        """ID test"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str_method(self):
        """ str method test"""
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """Save method test"""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        """to_dict method test"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_deserialization(self):
        """Deserialization test"""
        data = {
                'id': 'your_unique_id',
                'created_at': '2023-10-12T10:30:00.000000',
                'updated_at': '2023-10-12T12:45:00.000000',
                'other_attribute': 'value',
                }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, 'your_unique_id')
        self.assertEqual(instance.created_at.isoformat(), '2023-10-12T10:30:00.000')
        self.assertEqual(instance.updated_at.isoformat(), '2023-10-12T12:45:00.000')
        self.assertEqual(instance.other_attribute, 'value')



if __name__ == "__main__":
    unittest.main()
