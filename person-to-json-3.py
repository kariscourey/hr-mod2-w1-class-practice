# his is the same problem as the previous two. Now, it's just the function signature. Try to create the person_to_json function without referring back to your previous tries. If you do get stuck, take a peek.

# The person_to_json function gets an instance of the Person class, creates a dictionary that has the name and age in it, converts the dictionary to JSON using the json.dumps function, then returns the JSON-formatted string returned from json.dumps.

# Here are some examples of the input and output of the function.

# Input is a Python value	Output is a JSON-formatted string
# Person(name="Baz", age=18)	'{"name": "Baz", "age": 18 }
# Person(name="Noor", age=29)	'{"name": "Noor", "age": 29 }
# None	"null"

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_json(person):

    if person is None:
        return json.dumps(None)

    d = {
        "name": person.name,
        "age": person.age,
    }

    return json.dumps(d)

    # pass  # Delete this pass when you're done
