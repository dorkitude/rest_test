#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by dorkitude on 2010-08-02.

"""
# Define all your API test cases here!

# resources.
    # A resource can be either a "collection" or a "member".
    # Only members can have child resources.

# conditions...
    # must have a response_field, which is a path through the response to the field in question
    # may have a type_requirement
        #test fails if the response_field's type doesn't match this requirement
        # NoneType - aka type(None) - this special case will also match
    # may have comparison_requirements
        # test fails if the response_field's value doesn't fulfill the comparison
    # may have a fail_message, which will be appended to the standard test failure message
    
# comparison_requirements...
    # must specify a value, against which the response_field is evaluated
    # must specify a comparator, which can be "response_field_equals", "response_field_greater_than", "response_field_less_than"
        # test fails if value doesn't properly compare to the response

# /* --------------------- comment --------------------- */
 

# don't forget the trailing slash!
api_base_url = 'http://www.yoursite.com/api/'
    
# Tester will automatically append these get parameters to all URLs in the format: &key1=value1&key2=value2
global_get_params = {
}



global_conditions = (
    {
        "response_field" : "error",
        "type_requirement" : type(False),
        "comparison_requirements" : (
            {
                "comparator" : "response_field_equals",
                "value" : False,
            }
        ),
    },
)

# Put cases here! I've included some example cases for you to use as references
cases = (
    # <case>
    {
        "resource" : {
            "name" : "player",
            "type" : "collection",
            "get_params" : { 
                "doesn't matter" : "cool"
            },
        },
        "conditions" : (
            {
                "response_field" : "result.id",
                "type_requirement" : type(1),
                "fail_message" : "Player was missing the id field",
            },
            {
                "response_field" : "result.discovered_planet_ids",
                "type_requirement" : type(list()),
            },
        ), # /conditions
    }, # </case>
    
    # <case>
    {
        "resource" : {
            "name" : "gameObjectType",
            "type" : "collection",
        },
        "conditions" : (
            {
                "response_field" : "result.planet",
                "type_requirement" : type(list()),
                "fail_message" : "Player was missing the id field",
            },
            {
                "response_field" : "result.discovered_planet_ids",
                "type_requirement" : type(list()),
                "fail_message" : "Player was missing the id field",
            },
        ), # /conditions
    }, # </case>
    
)
    




