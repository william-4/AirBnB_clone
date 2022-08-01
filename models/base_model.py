#!/usr/bin/python3
"""Base model
"""
import datetime
import uuid


class BaseModel:
    """It defines all the common attributes for other classes"""
    id = 0
    created_at = 0
    update_at = 0
    name = ""
    my_number = None

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        self.name

    def __str__(self):
        """Method that returns a string representation of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at with current datetime"""
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """Returns dictionary containing all key/values of __dict__"""
        dictionary = {}
        dictionary["my_number"] = self.my_number
        dictionary["name"] = self.name
        dictionary["__class__"] = type(self).__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["id"] = self.id
        dictionary["created_at"] = self.created_at.isoformat()
        return dictionary
