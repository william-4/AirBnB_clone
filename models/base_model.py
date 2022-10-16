#!/usr/bin/python3
"""Base model
"""
from datetime import datetime
import uuid
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """It defines all the common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Method that returns a string representation of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing all key/values of __dict__"""
        dictionary = dict(self.__dict__)
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["__class__"] = type(self).__name__
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary
