#!/usr/bin/python3
"""Defines a class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates an instance of the class User.
    Attr:
        1. email: User email.
        2. password: User password.
        3. first_name: First name of the user.
        4. last_name: Last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
