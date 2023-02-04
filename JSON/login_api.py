from requests import request
from json import loads


url = "https://reqres.in/api/login"

json_payload = { "email": "eve.holt@reqres.in", "password": "cityslicka" }
# json_payload = { "email": "eve.holt@reqres.in"}

response = request("POST", url, json=json_payload)

if response.status_code == 200:
    print("PASS")
else:
    print("FAIL")

json_text = response.text

rp = loads(json_text)

if rp['token'] == "QpwL5tke4Pnpja7X4":
    print("PASS")
else:
    print("FAIL")
