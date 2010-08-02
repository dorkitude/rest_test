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
    
    #automatically append these get parameters
    GET_PARAMS = {
        'version' : '00033',
        'session' : '{"session_key":"2.7OtyhOYmizJ74cAsMnKebQ__.3600.1280782800-1903607","uid":"1903607","expires":1280782800,"secret":"8rRrl78GOrUJCQtB_jkh7Q__","access_token":"144297712254801|2.7OtyhOYmizJ74cAsMnKebQ__.3600.1280782800-1903607|dIKw5oMlCdGGXGfZ0UAp3tWEtxs.","sig":"db95490b7856486f0b21a4be09d22d95"}'
    }
    
    # Tell rest_test about your API
    BASE_URL = 'zootopia.dv.tbxing.com/frontend_dev.php/api/'
    