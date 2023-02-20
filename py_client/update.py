import requests

endpoint = "http://localhost:8000/api/products/1/update"

data = {"title": "Good news, everyone!", "price": 666.66}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
