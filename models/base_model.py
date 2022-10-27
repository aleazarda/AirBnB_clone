#!/usr/bin/python3
"""Defines the class BaseModel."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes and methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Instantiation of the BaseModel class.
        Args:
             1. args: Not used.
             2. kwargs: key word arguments.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if (k == "created_at" or k == "updated_at"):
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary of BaseModel instance."""
        d1 = self.__dict__.copy()
        d1["created_at"] = self.created_at.isoformat()
        d1["updated_at"] = self.updated_at.isoformat()
        d1["__class__"] = self.__class__.__name__
        return d1

    def __str__(self):
        """String representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
