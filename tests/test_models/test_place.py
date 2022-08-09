#!/usr/bin/python3
"""Test module for place.py
"""
from models.place import Place
from unittest import TestCase
import models


class TestPlace_documentation(TestCase):
    """Tests for the documentation of Place"""

    def test_module_docs(self):
        """Tests for the presence of the module's doc string"""
        self.assertTrue(len(models.place.__doc__) > 0)

    def test_class_docs(self):
        """Tests for the presence of the Place doc string"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_methods_docs(self):
        """Tests for the presence of the methods doc string"""
        callables = [f for f in dir(Place) if callable(getattr(Place, f))][22:]
        for func in callables:
            self.assertTrue(len(func.__doc__) > 0)


class TestPlace_attributes(TestCase):
    """Tests for the attributes of Place"""

    def test_name_type(self):
        """Verifies the type of the name attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.name, str))

    def test_city_id_type(self):
        """Verifies the type of the name attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.city_id, str))

    def test_user_id_type(self):
        """Verifies the type of the name attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.user_id, str))

    def test_description_type(self):
        """Verifies the type of the description attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.description, str))

    def test_number_rooms_type(self):
        """Verifies the type of the number_rooms attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.number_rooms, int))

    def test_number_bathrooms_type(self):
        """Verifies the type of the number_bathrooms attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.number_bathrooms, int))

    def test_max_guest_type(self):
        """Verifies the type of the max_guest attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.max_guest, int))

    def test_price_by_night_type(self):
        """Verifies the type of the price_by_night attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.price_by_night, int))

    def test_latitude_type(self):
        """Verifies the type of the latitude attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.latitude, float))

    def test_longitude_type(self):
        """Verifies the type of the longitude attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.longitude, float))

    def test_amenity_ids_type(self):
        """Verifies the type of the amenity_ids attribute"""
        place1 = Place()
        self.assertTrue(isinstance(place1.amenity_ids, list))

    def test_amenity_ids_elements_type(self):
        """Verifies the type of the amenity_ids attribute"""
        place1 = Place()
        for element in place1.amenity_ids:
            self.assertTrue(isinstance(element, str))


if __name__ == "__main__":
    unittest.main()
