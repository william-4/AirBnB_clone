#!/usr/bin/python3
"""Test module for user.py
"""
from models.user import User
from unittest import TestCase
import models


class TestUser_documentation(TestCase):
    """Tests for the documentation of User"""

    def test_module_docs(self):
        """Tests for the presence of the module's doc string"""
        self.assertTrue(len(models.user.__doc__) > 0)

    def test_class_docs(self):
        """Tests for the presence of the User doc string"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_methods_docs(self):
        """Tests for the presence of the methods doc string"""
        callables = [f for f in dir(User) if callable(getattr(User, f))][22:]
        for func in callables:
            self.assertTrue(len(func.__doc__) > 0)


class TestUser_attributes(TestCase):
    """Tests for the attributes of User"""

    def test_email_type(self):
        """Verifies the type of the email attribute"""
        user1 = User()
        self.assertTrue(isinstance(user1.email, str))

    def test_password_type(self):
        """Verifies the type of the password attribute"""
        user1 = User()
        self.assertTrue(isinstance(user1.password, str))

    def test_first_name_type(self):
        """Verifies the type of the first_name attribute"""
        user1 = User()
        self.assertTrue(isinstance(user1.first_name, str))

    def test_last_name_type(self):
        """Verifies the type of the last_name attribute"""
        user1 = User()
        self.assertTrue(isinstance(user1.last_name, str))


if __name__ == "__main__":
    unittest.main()
