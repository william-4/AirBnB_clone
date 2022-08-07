#!/usr/bin/python3
""" Defines User module """


from models.base_model import BaseModel


class User(BaseModel):
    """Defines the class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
