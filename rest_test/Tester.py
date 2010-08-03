#!/usr/bin/env python
# encoding: utf-8
"""
Ui.py

Created by dorkitude on 2010-08-02.
"""

import sys
import getopt
import mechanize
import logging
import test_setup
import json
import datetime

help_message = '''
The help message goes here.
'''


class Tester(Exception):
    browser = mechanize.Browser()

    def execute(self):
        cases = test_setup.cases
                
        # logging.debug('before for')
        for k,v in enumerate(cases):
            self.run_test_case(v)
        
    def run_test_case(self, case):
        output("running test case: ")
        response = self.get_response_dictionary(case)
        conditions = [test_setup.global_conditions]
        
        
    
    def get_response_dictionary(self, case):
        if case['resource']['type'] == 'collection':
            url = test_setup.api_base_url + case['resource']['name'] + '?'
        
        # append global key-value pairs
        for key in test_setup.global_get_params:
            value = test_setup.global_get_params[key]
            url += key + '=' + value + '&'            
        # append additional key-value pairs if specified in the case
        if case['resource'].has_key('additional_params'):
            for key in case['resource']['additional_params']:
                value = case['resource']['additional_params'][key]
                url += key + '=' + value + '&'

        pretty_name = case['resource']['name'] + 'Collection'

        self.test_url(url, pretty_name)
        
    
    def condition_passes(self, condition, response):
        pass
            
    def test_resource(self, resource):
        if resource['type'] == 'collection':
            self.test_resource_collection(resource)
    
    def test_url(self, url, pretty_name):
        start = datetime.datetime.now()
        # print "\n\ntesting %s with this url: %s" % (pretty_name, url)
        output("\n\ntesting %s..." % (pretty_name))
        browser = self.browser
        response = browser.open(url)
        finish = datetime.datetime.now()
        
        logging.debug('name=%s and url=%s' % (pretty_name, url))
        timedelta = (finish - start)
        response_ms = timedelta.microseconds/1000
        output('server responded in ' + str(response_ms) + ' ms')

        # logging.debug(response.get_data())
        response_json= response.get_data()
        response_dict = json.loads(response_json)
    
    def output(self, message, newline=False):
        if newline:
            print(message)
        else:
            sys.stdout.write(message)