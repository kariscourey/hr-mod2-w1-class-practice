import json

# loads converts JSON-formatted string to Python values
# dumps converts Python values to JSON-formatted strings

ten = json.loads("10")
print(ten)
print(type(ten))


nope = json.loads("null")
print(nope)
print(type(nope))


not_true = json.loads("false")
print(not_true)
print(type(not_true))


lst = json.loads("[10, 20, 30]")
print(lst)
print(type(lst))

for i in lst:
    print(type(i))


book = json.loads('{"title": "Hench", "author": "Natalie Zina Walschots", "sold": 513000}')
print(book)
print(type(book))

dumped_book = json.dumps(book)
print(dumped_book)
print(type(dumped_book))
