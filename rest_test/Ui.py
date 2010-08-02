#!/usr/bin/env python
# encoding: utf-8
"""
Ui.py

Created by dorkitude on 2010-08-02.
"""

import sys
import getopt
from Datastore import *
import mechanize
import logging
import api_resources as resources
import json

help_message = '''
The help message goes here.
'''


class Ui(Exception):
    def execute(self):
        print "What's your name?"

        self.run_tests()
        
        
        
    def run_tests(self):
        col = resources.collections
        
        ds = Datastore()
        GET = ds.GET_params
        logging.debug(json.dumps({'GET' : GET}))
        
        