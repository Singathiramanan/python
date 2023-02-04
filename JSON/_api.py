from requests import request
from json import loads
from csv import reader

def read_csv():
    records = [ ]
    with open("../data_files/bank.csv") as f:
        rows = reader(f)
        headers = next(rows)    # skip headers
        for row in rows:
            records.append({"code": row[0], "expected_branch": row[1]})
    return records

data = read_csv()

for item in data:
    url = f"https://ifsc.razorpay.com/{item['code']}"
    
    print(f"hitting the endpoint or url {url}")
    
    # programatically hitting the request
    response = request("GET", url)

    # getting the actual response in text format using property "text"
    json_text = response.text

    # loads function converts a JSON string into a python data structure 
    # this process is called as de-serilisation
    rsp = loads(json_text)

    if rsp['BRANCH'] == item['expected_branch']:
        print("PASS")
    else:
        print("FAIL")