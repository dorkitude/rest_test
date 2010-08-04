#!/usr/bin/env python
# encoding: utf-8
"""
Ui.py

Created by dorkitude on 2010-08-02.
"""

import sys
import getopt
import mechanize
import test_setup
import json
import datetime
import string
import settings
import logging

help_message = '''
The help message goes here.
'''

class TestCaseException(Exception):
    def __init__(self, condition, msg=''):
        if msg == '':
            msg = 'no custom failure message specified'
        self.msg = "%s Field 'response.%s' failed GENERIC test: %s" % (condition['pretty_resource_name'], condition['response_field'], msg)

class TestCaseTypeException(TestCaseException):
    def __init__(self, condition, msg=''):
        if msg == '':
            msg = 'no custom failure message specified'
        self.msg = "%s Field 'response.%s' failed TYPE test: %s" % (condition['pretty_resource_name'], condition['response_field'], msg)

class TestCaseComparatorException(TestCaseException):
    def __init__(self, condition, msg=''):
        if msg == '':
            msg = 'no custom failure message specified'
        self.msg = "%s Field 'response.%s' failed COMPARITOR test: %s" % (self.condition['pretty_resource_name'], condition['response_field'], msg)
    

class Tester():
    browser = mechanize.Browser()
    
    successes = []
    failures = []

    def execute(self):
        output('', True);
        cases = test_setup.cases
        for k,v in enumerate(cases):
            self.run_test_case(v)
        output('', True);
        if len(self.failures) > 0:
            output("\n\n\nFailure Breakdown", True)
            output("--------------------------------------", True)
            for e in self.failures:
                output(e.msg, True)
            output("--------------------------------------", True)
        
    def run_test_case(self, case):
        self.pretty_resource_name = case['resource']['name'] + case['resource']['type'].capitalize()
        output("\n\nrunning test case: %s" % (self.pretty_resource_name))

        response = self.get_response_dictionary(case)
        conditions = list(test_setup.global_conditions)
                
        for condition in case['conditions']:
            conditions.append(condition)
            
        i = 0
        for condition in conditions:
            i += 1
            condition['pretty_resource_name'] = self.pretty_resource_name
            try:
                output("\n  - testing 'response.%s'" % (condition['response_field']))
                self.check_condition(response, condition)
                output("...passed")
            except TestCaseException, e:
                self.failures.append(e)
                output("...FAILED!!!!!!!!!!!")
            else:
                self.successes.append(condition)
        
        output("\n--------------------------------------", newline=True)

    def check_condition(self, response, condition):
        field = self.find_response_field(response, condition['response_field'])
                
        if condition.has_key('type_requirement'):
            if type(field) != condition['type_requirement']:
                raise TestCaseTypeException(condition, "%s instead of %s" % (type(field).__name__, condition['type_requirement'].__name__))
                
    
    def find_response_field(self, response, field_string):
        node_stack = field_string.split(".")
        node_stack.reverse()
        current_field = response
        # dig down into the response dictionary until we can't find the next field or we get to the end of node stack
        while len(node_stack) > 0:
            node = node_stack.pop()
            if current_field.has_key(node):
                current_field = current_field[node]
            else:
                field_value = None
                break
        
        
        if 'field_value' not in locals():
            field_value = current_field
        
        return field_value
    
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

        self.pretty_resource_name = case['resource']['name'] + case['resource']['type'].capitalize()

        start = datetime.datetime.now()
        output("\n--------------------------------------\nfetching %s..." % (self.pretty_resource_name))
        browser = self.browser
        response = browser.open(url)
        finish = datetime.datetime.now()
        
        logging.debug('name=%s and url=%s' % (self.pretty_resource_name, url))
        timedelta = (finish - start)
        response_ms = timedelta.microseconds/1000
        output('server responded in ' + str(response_ms) + ' ms\n')

        logging.debug(response.get_data())
        # print "\n" + response.get_data() + "\n"
        response_json= response.get_data()
        response_dict = json.loads(response_json)
        
        return response_dict
        
    
    def condition_passes(self, condition, response):
        pass
            
    def test_resource(self, resource):
        if resource['type'] == 'collection':
            self.test_resource_collection(resource)
        
def output(message, newline=False):
    if newline:
        print(message)
    else:
        sys.stdout.write(message)