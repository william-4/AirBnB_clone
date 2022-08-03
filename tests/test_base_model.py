#!/usr/bin/python3
"""Test module for base_model.py
"""
from unittest import TestCase
import models.base_model
import re

base_class = models.base_model.BaseModel


class TestDocumentation(TestCase):
    """Tests for the documentation of BaseModel"""

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


if __name__ == '__main__':
    unittest.main()
