#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json
from copy import deepcopy
from models.base_model import BaseModel


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
                data = {key: BaseModel.to_dict(value)
                        for key, value in temp_objects.items()}
                json.dump(data, file)
        

    def reload(self):
        """
        Deserializes a json File to __objects
        Only if the file exists in path
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

            for ser_data in data.values():
                obj_cls = ser_data.get("__class__")
            
                if obj_cls:
                    obj_class = eval(obj_cls)
                    obj_instance = obj_class(**ser_data)
                    self.new(obj_instance)

        except Exception:
            pass



    