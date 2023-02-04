from requests import request
from json import loads

url = "https://reqres.in/api/register"

payload = {
    "email": "sydney@fife"
}

response = request("POST", url, json=payload)

if response.status_code == 400:
    print("PASS")
else:
    print("FAIL")

json_text = response.text

rsp = loads(json_text)

if rsp['error'] == "Missing password":
    print("PASS")
else:
    print("FAIL")