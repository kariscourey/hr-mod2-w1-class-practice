import requests

res = requests.get('https://randomuser.me/api/')
res = requests.get('https://randomuser.me/api?results=10/')
# print(res)
# print(res.json())
# print(res.json()['results'])  # prints all people if results != #
# print(res.json()['results'][0])  # prints first person
# print(res.json()['results'][0]['gender'])
# print(res.json()['results'][0]['name']['first'])
# print(f"Hello, {res.json()['results'][0]['name']['first']}")
