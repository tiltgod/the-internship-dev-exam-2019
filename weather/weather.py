""" -*- coding: python(3.7.1) -*-
    author: Napasin Hongngern """
""" weather """

import json
import xmltodict
import os

xml_input = input()# Get a file as input
filename_w_ext = os.path.basename(xml_input) # Get basename from file
filename = os.path.splitext(filename_w_ext)[0] # Get only filename from basename

with open(xml_input, 'r') as raw_xml: # Read a file and get all of the file as string
    xml_str = raw_xml.read()

converted_json = json.dumps(xmltodict.parse(xml_str, attr_prefix='', cdata_key=''), indent=4) # Converting file by using xmltodict library and get rid of prefixes

json_output = filename + ".json" # create output 's filename
print(json_output)

with open(json_output, 'w') as json_writer: # write a json file
    json_writer.write(converted_json)



 

 

