# The person_to_json function gets an instance of the Person class, creates a dictionary that has the name and age in it, converts the dictionary to JSON using the json.dumps function, then returns the JSON-formatted string returned from json.dumps.

# Here are some examples of the input and output of the function.

# Input is a Python value	Output is a JSON-formatted string
# Person(name="Baz", age=18)	'{"name": "Baz", "age": 18 }'
# Person(name="Noor", age=29)	'{"name": "Noor", "age": 29 }'
# None	"null"
# We've included some pseudocode and a partially-complete function for you to work with.

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_json(person):
    # If the person is None, then return the JSON-formatted
    # version of None
    if person is None:
        # Finish this return statement with json.dumps(None)
        return json.dumps(None)

    # Create a dictionary from the Person instance
    d = {
        "name":  person.name,  # Put person.name before the comma
        "age":   person.age,  # Put person.age before the comma
    }

    # Pass the d variable to json.dumps on the
    # right-hand side of the assignment operator =
    result = json.dumps(d)

    # Return the value of result as the last line
    return result
