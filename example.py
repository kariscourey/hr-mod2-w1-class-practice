import json

# some_json = '{"name":"Warren", "age": 33, "height":5.11}'
# some_dict = json.loads(some_json)

# print(some_dict)
# print(f"Your name is {some_dict['name']}")

# some_other_dict = {
#     "hotel": "Marriot",
#     "roomNumber": 5,
#     "rooms": [{id:1, "room_number":"b12"},{id:2, "room_number":"b33"}],
#     "address": {
#         "street": "2121 N 21nd Street",
#         "state": "PA",
#         "city": "Philly"
#     }
# }


# def ourDump(dict):
#     json = "{"
#     for key in dict:
#         json += f'"{key}":{dict[key]}",'

#     return json + "}"

# #Dictionary to JSON
# some_other_json = json.dumps(some_other_dict)
# print('json:', some_other_json)

convention = {
    "id": 12221,
    "name": "The Best",
    "location_id": 1231,
    "description": "Description of convention",
    "isVirtual": False,
}

print(convention["name"])
print(f'get method: {convention.get("audienceCount", 100)}')


print("----------------")
for key in convention:
    print(f"key {key} contains value {convention[key]}")
print("----------------")



# print(convention.keys())
# print(convention.values())
# print(convention.items())


# print(some_json["name"])  # doesn't work

# need to convert json string to its equivalent inside of a language (in this case, a dict)
# use loads
