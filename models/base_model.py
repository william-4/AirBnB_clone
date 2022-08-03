#!/usr/bin/python3
"""Base model
"""
from datetime import datetime
import uuid


class BaseModel:
    """It defines all the common attributes for other classes"""
    id = 0
    created_at = 0
    my_number = None
    update_at = 0
    name = ""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.my_number = None
        self.updated_at = self.created_at
        self.name = ""

        if kwargs is not None:
            for key, value in kwargs.items():
                if key in  ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value


    def __str__(self):
        """Method that returns a string representation of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at with current datetime"""
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


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
