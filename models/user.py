"""A module for User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class to handle user specific attributes
    Parent Class: BaseModel

    Attributes:
            email - user email address
            password - user password
            first_name - user first name
            last_name - user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
