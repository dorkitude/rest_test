#!/usr/bin/env python
# encoding: utf-8
"""
settings.py

Created by dorkitude on 2010-08-02.
"""

import sys
import os
import unittest
import logging


class settings:
    def __init__(self):
        pass
        
    #datastore
    FLAT_FILE_PATH = 'flat_files'
    
    #logging
    LOG_FILENAME = 'debug.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    