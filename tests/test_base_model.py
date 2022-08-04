#!/usr/bin/python3
"""Test module for base_model.py
"""
from unittest import TestCase
import models.base_model
import re
from datetime import datetime


base_class = models.base_model.BaseModel


class Test_Task3(TestCase):
    """Tests for the documentation of BaseModel and Task 3"""

    def test_module_docs(self):
        """Tests for the presence of the module doc string"""
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_class_docs(self):
        """Tests for the presence of the BaseModel doc string"""
        self.assertTrue(len(base_class.__doc__) > 0)

    def test_methods_docs(self):
        """Tests for the presence of the BaseModel doc string"""
        callables = [func for func in dir(base_class) if callable(
                    getattr(base_class, func))][22:]
        for func in callables:
            self.assertTrue(len(func.__doc__) > 0)

    def test_datetime_format(self):
        """Verifies the format of the datetime"""
        datetime_pattern = re.compile(r'(?:20\d{2})-(?:0[1-9]|1[012])-'
                                      r'(?:0[1-9]|[12]\d|3[01])T'
                                      r'(?:[01]\d|2[0-3]):(?:[0-5]\d):'
                                      r'(?:[0-5]\d)\.\d{6}'
        )
        base_model_instance = base_class()
        base_dict = base_model_instance.to_dict()
        self.assertTrue(datetime_pattern.match(base_dict['created_at']))

class Test_Task4(TestCase):
    """Tests for task 4"""

    def test_created_at(self):
        """Verifies the type of the attribute created_at"""
        my_model = base_class()
        self.assertTrue(isinstance(my_model.created_at, datetime))
        my_model_json = my_model.to_dict()
        self.assertTrue(isinstance(my_model_json["created_at"], str))
        my_new_model = base_class(**my_model_json)
        self.assertTrue(isinstance(my_new_model.created_at, datetime))

    def test_updated_at(self):
        """Verifies the type of the attribute updated_at"""
        my_model = base_class()
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        my_model_json = my_model.to_dict()
        self.assertTrue(isinstance(my_model_json["updated_at"], str))
        my_new_model = base_class(**my_model_json)
        self.assertTrue(isinstance(my_new_model.updated_at, datetime))

    def test_compare_instances(self):
        """Verifies that my_model is not my_new_model"""
        my_model = base_class()
        my_model_json = my_model.to_dict()
        my_new_model = base_class(**my_model_json)
        self.assertFalse(my_model is my_new_model)

class Test_Task5(TestCase):

        

    
        



if __name__ == '__main__':
    unittest.main()
