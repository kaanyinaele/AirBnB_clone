#!/usr/bin/python3
'''
User class
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Class User inherits from BaseModel
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """
        init
        """
        super().__init__(*args, **kwargs)
