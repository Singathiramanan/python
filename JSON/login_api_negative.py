from requests import request
from json import loads

url = "https://reqres.in/api/login"

json_payload = { "email": "peter@klaven" }

response = request("POST", url, json=json_payload)

if response.status_code == 400:
    print("PASS")
else:
    print("FAIL")

json_text = response.text

rp = loads(json_text)

if rp['error'] == "Missing password":
    print("PASS")
else:
    print("FAIL")
