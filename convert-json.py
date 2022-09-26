# Consider the function convert_json. It's input parameter, json_formatted_string, will contain a JSON-formatted string. The json module is already imported for you. Use the loads function of the json module to convert the value in json_formatted_string and return that value.

# You should only have to write one or two lines in this function to use the json.loads function, then return whatever it returns.

import json

def convert_json(json_formatted_string):
    return json.loads(json_formatted_string)
