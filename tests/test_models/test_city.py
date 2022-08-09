#!/usr/bin/python3
"""Test module for city.py
"""
from models.city import City
from unittest import TestCase
import models


class TestCity_documentation(TestCase):
    """Tests for the documentation of City"""

    def test_module_docs(self):
        """Tests for the presence of the module's doc string"""
        self.assertTrue(len(models.city.__doc__) > 0)

    def test_class_docs(self):
        """Tests for the presence of the City doc string"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_methods_docs(self):
        """Tests for the presence of the methods doc string"""
        callables = [f for f in dir(City) if callable(getattr(City, f))][22:]
        for func in callables:
            self.assertTrue(len(func.__doc__) > 0)


class TestCity_attributes(TestCase):
    """Tests for the attributes of City"""

    def test_name_type(self):
        """Verifies the type of the name attribute"""
        city1 = City()
        self.assertTrue(isinstance(city1.name, str))

    def test_state_id_type(self):
        """Verifies the type of the name attribute"""
        city1 = City()
        self.assertTrue(isinstance(city1.state_id, str))


if __name__ == "__main__":
    unittest.main()
