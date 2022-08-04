#!/usr/bin/python3
"""The file storage module
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """A class that serializes and deserializes instances to JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictioanry __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file file.json"""
        with open(FileStorage.__file_path, "w") as f:
            new_obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass
