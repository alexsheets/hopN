import requests

#---------------------------------------------------

endpoint = 'http://localhost:8000/api/breweries/'

data = {
    'name': 'new brewery',
    'description': 'it sucks',
    'email': 'fake@gmail.com',
    'website': '',
    'rating': '6.9',
    'phn_number': '2258888888',
    'address': 'cum on 420 st'
}
get_resp = requests.post(endpoint, json=data)
print(get_resp.json())