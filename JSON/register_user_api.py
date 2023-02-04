from requests import request
from json import loads

url = "https://reqres.in/api/register"

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = request("POST", url, json=payload)

print(response.status_code)

json_text = response.text

rsp = loads(json_text)

if rsp['id'] == 4:
    print("PASS")
else:
    print("FAIL")

if rsp['token'] == "QpwL5tke4Pnpja7X4":
    print("PASS")
else:
    print("FAIL")