# This is the same function that you just completed. This time, though, there is only the pseudocode. Please try to complete it without referring to your previous attempt. If you do get stuck, take a peek.

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
    # If the person is None
    if person is None:
        # return the JSON-formatted version of None
        return json.dumps(None)

    # Create a dictionary from the Person instance
    d = {
        "name": person.name,
        "age": person.age
    }

    # Pass the d variable to json.dumps on the
    # right-hand side of the assignment operator =
    result = json.dumps(d)

    # Return the value of result as the last line
    return result

    # pass  # Delete this pass when you're done
