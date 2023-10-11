#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json
from copy import deepcopy
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
     Class for file storage implementation
    """

    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
        Returns dictionary representation of all objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the object with the key
        <object class name>.id

        Args:
            object(obj): object to write

        """
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """
        serializes __objects to json file.
        file path = __file_path
        """
        temp_objects = deepcopy(self.__objects)
        with open(self.__file_path, 'w+') as file:
                data = {key: value.to_dict()
                        for key, value in temp_objects.items()}
                json.dump(data, file)
        

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass



    