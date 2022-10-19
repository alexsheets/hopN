import requests

# localhost:8000/api/?this_arg=this_value

endpoint = "http://localhost:8000/api/"

# get_resp = requests.get(endpoint, params={"abc": 123}, json={"query": "hello"})
post_resp = requests.post(endpoint, json={'name': 'tin roof', 'description': 'nah'})

# HTTP REQ -> HTML
# rest api http req -> json
# javascript object notation
print(post_resp.json())