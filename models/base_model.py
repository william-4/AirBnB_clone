#!/usr/bin/python3
"""Base model
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """It defines all the common attributes for other classes"""
    # id = 0
    # created_at = 0
    # my_number = None
    # update_at = 0
    # name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    pttrn = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value,
                                                           pttrn)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.my_number = None
            self.updated_at = self.created_at
            self.name = ""
            models.storage.new(self)

    def __str__(self):
        """Method that returns a string representation of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at with current datetime"""
        models.storage.save()
        self.update_at = datetime.now()

    def to_dict(self):
        """Returns dictionary containing all key/values of __dict__"""
        dictionary = {}
        dictionary["id"] = self.__dict__["id"]
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["__class__"] = type(self).__name__
        dictionary["my_number"] = self.__dict__["my_number"]
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["name"] = self.__dict__["name"]
        return dictionary
