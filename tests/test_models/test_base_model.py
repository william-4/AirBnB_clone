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


class TestBaseModel_representation(TestCase):
    """Tests the representation used by BaseModel"""

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456789"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456789)", bmstr)
        self.assertIn("'id': '123456789'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

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

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)
        second_updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

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


class TestBaseModel_to_dict(TestCase):
    """Tests the to_dict method of BaseMode"""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(isinstance(bm.to_dict(), dict))

    def test_to_dict_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        bm.name = "betty"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertTrue(isinstance(bm_dict["created_at"], str))
        self.assertTrue(isinstance(bm_dict["updated_at"], str))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_and_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
