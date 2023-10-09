"""Base Model for the AirBnB project"""
import uuid
from datetime import datetime


class BaseModel():
    """This is superclass for the entire project
    It takes no args by default and serves as Parent class"""
    def __init__(self, *args, **kwargs):
        DateF= "%Y-%m-%dT%H:%M:%S.%f"
        """Init an instance with these default values"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
          for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, DateF)
                elif key != "__class__":
                    self.__dict__[key] = value

    def __str__(self):
        """Return custom dict representation of the instance """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update modifed time of the instance
        More implementation will be added later on (WIP method)"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dict representation of the instance with additional
        attributes and iso formatted date-time"""
        dict_rep = vars(self)
        dict_rep["__class__"] = self.__class__.__name__
        for key, value in dict_rep.items():
            if key == "updated_at" or key == "created_at":
                dict_rep[key] = value.isoformat(timespec="microseconds")
        return dict_rep
