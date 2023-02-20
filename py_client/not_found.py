import requests

endpoint = "http://localhost:8000/api/products/1234345645671345"

get_response = requests.get(endpoint)

print(get_response.json())
