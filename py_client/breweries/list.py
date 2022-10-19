import requests

#--------------------------------------

endpoint = 'http://localhost:8000/api/breweries/'

get_resp = requests.get(endpoint)
print(get_resp.json())