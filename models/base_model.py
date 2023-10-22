#!/usr/bin/python3
"""BaseModel Class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """constructor to make instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if "id" not in kwargs.keys():
                    self.id = str(uuid4())
                if "created_at" not in kwargs.keys():
                    self.created_at = datetime.now()
                if "updated_at"not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ return string representation of the object"""
        return ('[' + type(self).__name__ + '] (' + str(self.id) +
                ') ' + str(self.__dict__))

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        tempDict = self.__dict__.copy()
        tempDict["__class__"] = self.__class__.__name__
        tempDict["created_at"] = self.created_at.isoformat()
        tempDict["updated_at"] = self.updated_at.isoformat()
        return tempDict
    
    def delete(self):
        """Delete current instance"""
        models.storage.delete(self)
