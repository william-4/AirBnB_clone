#!/usr/bin/python3
"""Test module for amenity.py
"""
from models.amenity import Amenity
from unittest import TestCase
import models


class TestAmenity_documentation(TestCase):
    """Tests for the documentation of Amenity"""

    def test_module_docs(self):
        """Tests for the presence of the module's doc string"""
        self.assertTrue(len(models.amenity.__doc__) > 0)

    def test_class_docs(self):
        """Tests for the presence of the Amenity doc string"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_methods_docs(self):
        """Tests for the presence of the methods doc string"""
        callables = [f for f in dir(Amenity) if callable(
                            getattr(Amenity, f))][22:]
        for func in callables:
            self.assertTrue(len(func.__doc__) > 0)


class TestAmenity_attributes(TestCase):
    """Tests for the attributes of Amenity"""

    def test_name_type(self):
        """Verifies the type of the name attribute"""
        amenity1 = Amenity()
        self.assertTrue(isinstance(amenity1.name, str))


if __name__ == "__main__":
    unittest.main()
