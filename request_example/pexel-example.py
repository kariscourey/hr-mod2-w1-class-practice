import requests

PEXEL_API_KEY = "563492ad6f917000010000017d5e4e265e26443dad9c1211f0c795fc"
url = "https://api.pexels.com/v1/search?query=Philadelphia+PA&per_page=1"
headers = {
    'Authorization': PEXEL_API_KEY,
}

res = requests.get(url, headers=headers)  # in addn to premade headers, adding our headers
print(res.json())
