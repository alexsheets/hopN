import requests

#------------------------------------------

endpoint = "http://localhost:8000/api/breweries/1/"

get_resp = requests.get(endpoint)
print(get_resp.json())