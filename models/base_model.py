#!/usr/bin/python3
"""Base model
"""


class BaseModel:
    """It defines all the common attributes for other classes"""
    id = 0
    created_at = 0
    update_at = 0

    def __init__(self):
        # self.id =
        # self.created_at =
        # self.updated_at =

    def __str__(self):
        """Method that returns a string representation of the class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
