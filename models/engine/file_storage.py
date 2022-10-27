#!/usr/bin/python3
"""Defines a class FileStorage."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes/Deserializes instances/JSON file.
    Attr:
        1. file_path: String path to JSON file.
        2. objects: Dictionary (Init-Empty) store objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.
        Args:
            1. obj: Object to be set in __objects.
        """
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        dict1 = FileStorage.__objects
        obj_dict = {k: dict1[k].to_dict() for k in dict1.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for v in objdict.values():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(cls_name)(**v))
        except FileNotFoundError:
            return
