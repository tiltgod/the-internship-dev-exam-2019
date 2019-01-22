""" -*- coding: python(3.7.1) -*-
    author: Napasin Hongngern """
""" weather """

import json
import xmltodict
import os

xml_input = input()
with open(xml_input, 'r') as raw_xml:
    xml_str = raw_xml.read()

converted_json = json.dumps(xmltodict.parse(xml_str, attr_prefix='', cdata_key=''), indent=4)

filename_w_ext = os.path.basename(xml_input)
filename = os.path.splitext(filename_w_ext)[0]
json_output = filename + ".json"
print(json_output)

with open(json_output, 'w') as json_writer:
    json_writer.write(converted_json)


 

 

