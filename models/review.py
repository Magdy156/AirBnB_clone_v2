#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Represents a Review'''
    place_id = ""
    user_id = ""
    text = ""
