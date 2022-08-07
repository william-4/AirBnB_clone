#!/usr/bin/python3
"""Test module for base_model.py
"""
from models.base_model import BaseModel
from unittest import TestCase
from datetime import datetime
from time import sleep
import models
import os
import re


class TestBaseModel_documentation(TestCase):
    """Tests for the documentation of BaseModel"""

    def test_module_docs(self):
        """Tests for the presence of the module doc string"""
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_class_docs(self):
        """Tests for the presence of the BaseModel doc string"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_methods_docs(self):
        """Tests for the presence of the BaseModel doc string"""
        callables = [func for func in dir(BaseModel) if callable(
                    getattr(BaseModel, func))][22:]
        for func in callables:
            self.assertTrue(len(func.__doc__) > 0)


class TestBaseModel_instantiation(TestCase):
    """Tests for the proper creation of instances of BaseModel"""

    def test_no_args_instantiation(self):
        bm = BaseModel()
        self.assertTrue(isinstance(bm, BaseModel))

    def test_id_is_public_str(self):
        bm = BaseModel()
        self.assertTrue(isinstance(bm.id, str))

    def test_updated_at_is_public_datetime(self):
        bm = BaseModel()
        self.assertTrue(isinstance(bm.updated_at, datetime))

    def test_created_at_is_public_datetime(self):
        bm = BaseModel()
        self.assertTrue(isinstance(bm.created_at, datetime))

    def test_two_models_unique_ids(self):
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.id, bm2.id)

    def test_two_models_diff_updated_and_created_at(self):
        bm = BaseModel()
        sleep(0.02)
        bm2 = BaseModel()
        self.assertLess(bm.created_at, bm2.created_at)
        self.assertLess(bm.updated_at, bm2.updated_at)

    def test_using_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="0001", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "0001")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_using_args_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(1, "2", id="0001", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "0001")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModel_datetime_format(TestCase):
    """Tests the format of the datetime used by BaseModel"""

    def test_datetime_format(self):
        """Verifies the format of the datetime"""
        datetime_pattern = re.compile(r'(?:20\d{2})-(?:0[1-9]|1[012])-'
                                      r'(?:0[1-9]|[12]\d|3[01])T'
                                      r'(?:[01]\d|2[0-3]):(?:[0-5]\d):'
                                      r'(?:[0-5]\d)\.\d{6}')
        base_model_instance = BaseModel()
        base_dict = base_model_instance.to_dict()
        self.assertTrue(datetime_pattern.match(base_dict['created_at']))


class TestBaseModel_save(TestCase):
    """Tests the save method for BaseModel"""

    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_args(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_saved_model_in_json_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == "__main__":
    unittest.main()
