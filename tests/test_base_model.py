#!/usr/bin/python3
"""Test module for base_model.py
"""
from unittest import TestCase
import models.base_model

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


if __name__ == '__main__':
    unittest.main()
