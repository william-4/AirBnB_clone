#!/usr/bin/python3
"""Test module for state.py
"""
from models.state import State
from unittest import TestCase
import models


class TestState_documentation(TestCase):
    """Tests for the documentation of State"""

    def test_module_docs(self):
        """Tests for the presence of the module's doc string"""
        self.assertTrue(len(models.state.__doc__) > 0)

    def test_class_docs(self):
        """Tests for the presence of the State doc string"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_methods_docs(self):
        """Tests for the presence of the methods doc string"""
        callables = [f for f in dir(State) if callable(getattr(State, f))][22:]
        for func in callables:
            self.assertTrue(len(func.__doc__) > 0)


class TestState_attributes(TestCase):
    """Tests for the attributes of State"""

    def test_name_type(self):
        """Verifies the type of the name attribute"""
        state1 = State()
        self.assertTrue(isinstance(state1.name, str))


if __name__ == "__main__":
    unittest.main()
