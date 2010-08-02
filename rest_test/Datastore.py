#!/usr/bin/env python
# encoding: utf-8
"""
Datastore.py

Created by dorkitude on 2010-08-02.
"""

import sys
import os
import unittest
from settings import *
import shelve


class Datastore:
    def __init__(self):
        pass

    @property
    def GET_params(self):
        if('_GET_params' not in locals()):
            GET = self._GET_params = {}
        
        GET = settings.GET_PARAMS
        
        return  GET
    
    def get_shelf(self, key):
        return shelve.open(settings.FLAT_FILE_PATH + '/' + key + '.' + settings.VERSION)

    

class DatastoreTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()