#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Represensts the city'''
    state_id = ""
    name = ""
