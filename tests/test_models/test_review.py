#!/usr/bin/python3
"""Test module for review.py
"""
from models.review import Review
from unittest import TestCase
import models


class TestReview_documentation(TestCase):
    """Tests for the documentation of Review"""

    def test_module_docs(self):
        """Tests for the presence of the module's doc string"""
        self.assertTrue(len(models.review.__doc__) > 0)

    def test_class_docs(self):
        """Tests for the presence of the Review doc string"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_methods_docs(self):
        """Tests for the presence of the methods doc string"""
        callables = [f for f in dir(Review) if callable(
                            getattr(Review, f))][22:]
        for func in callables:
            self.assertTrue(len(func.__doc__) > 0)


class TestReview_attributes(TestCase):
    """Tests for the attributes of Review"""

    def test_text_type(self):
        """Verifies the type of the text attribute"""
        review1 = Review()
        self.assertTrue(isinstance(review1.text, str))

    def test_place_id_type(self):
        """Verifies the type of the place_id attribute"""
        review1 = Review()
        self.assertTrue(isinstance(review1.place_id, str))

    def test_user_id_type(self):
        """Verifies the type of the user_id attribute"""
        review1 = Review()
        self.assertTrue(isinstance(review1.user_id, str))


if __name__ == "__main__":
    unittest.main()
