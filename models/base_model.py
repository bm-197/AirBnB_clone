"""Base Model for the AirBnB project"""
import uuid
import models
from datetime import datetime

class BaseModel():
    """This is superclass for the entire project
    Attributes:
                id - randomely generated uuid for each object
                created_at - init timestamp for an instance
                updated_at - update timestamp of an instance
                DateF - general timestamp format that will be used
                        on all instances
    Methods:
                __str__ : returns dict representation of an instance"""

    DateF = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Init an instance with provided dict or randomely generated values
            Args:
                *args: Not used at the moment
                **kwargs: dict representation of an object
                          init an object from the dict"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, self.DateF))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Return custom dict representation of the instance """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update modifed time of the instance
        More implementation will be added later on (WIP method)"""
        self.updated_at = datetime.now()
        models.storage.save()
        

    def to_dict(self):
        """Return dict representation of the instance with additional
        attributes and iso formatted date-time"""
        dict_rep = vars(self)
        dict_rep["__class__"] = self.__class__.__name__
        for key, value in dict_rep.items():
            if key == "updated_at" or key == "created_at":
                dict_rep[key] = value.isoformat(timespec="microseconds")
        return dict_rep
