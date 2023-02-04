from requests import request
from json import loads

emails = [
    ("hello.world", "failure"),
    ("hello.world@company.com", "success"),
    ("hello.world@", "failure"),
    ("hello.world@.com", "failure"),
    ("hello.world@company.gov.in", "success"),
    ("hello.world@company.edu", "success")
    ]

for email in emails:
    url = f"https://api.eva.pingutil.com/email?email={email[0]}"

    # returns a Request object
    response = request("GET", url)

    # getting json string from response object
    json_text = response.text

    # deserilising the json string
    rsp = loads(json_text)

    # actual status getting from the response
    actual_status = rsp['status']

    if actual_status == email[1]:
        print("PASS")
    else:
        print("FAIL")