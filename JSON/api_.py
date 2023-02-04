from requests import request
from json import loads

def test_login():
    payload = {
        "user_name": "admin",
        "password": "Password123"
    }
    response = request("POST", url="https://demoshoppingcartapi.herokuapp.com/login", json=payload)
    # convert response object into json text
    json_text = response.text
    # convert JSON text into python data structure (deserilisation)
    rsp = loads(json_text)
    # validate the response
    if rsp['status'] == "logged in":
        print("PASS")
    else:
        print("FAIL")

def test_register():
    url = "https://demoshoppingcartapi.herokuapp.com/register"
    payload = {
    "gender": "male",
    "first_name": "steve",
    "last_name": "jobs",
    "email": "email",
    "password": "Password123",
    "confirm_password": "Password123"
    }

    response = request("POST", url, json=payload)

    json_text = response.text

    rsp = loads(json_text)

    if rsp['message'] == "User registered successfully":
        print("PASS")
    else:
        print("FAIL")


def test_add_book():
    url = "https://demoshoppingcartapi.herokuapp.com/addbook"
    payload = {
    "title": "Jungle Book",
    "quantity": 1
    }
    response = request("POST", url, json=payload)
    json_text = response.text
    rsp = loads(json_text)

    if rsp['message'] == "Book added successfully":
        print("PASS")
    else:
        print("FAIL")


def test_remove_book():
    url = "https://demoshoppingcartapi.herokuapp.com/removebook"
    payload = {
    "title": "Jungle Book"
    }
    response = request("POST", url, json=payload)
    json_text = response.text
    rsp = loads(json_text)
    if rsp['message'] == "Book removed successfully":
        print("PASS")
    else:
        print("FAIL")

def test_payment():
    url = "https://demoshoppingcartapi.herokuapp.com/pay"
    payload = {
    "first_name": "steve",
    "last_name": "jobs",
    "card_type": "visa",
    "card_number": "1234123412341234",
    "expiry_month": "09",
    "expiry_year": "2026",
    "cvv_number": "123",
    "amount": "1200"
    }
    response = request("POST", url, json=payload)
    json_text = response.text
    rsp = loads(json_text)
    if rsp['message'] == "Payment successfull":
        print("PASS")
    else:
        print("FAIL")

def display_available_books():
    url = "https://demoshoppingcartapi.herokuapp.com/books"
    response = request("GET", url)
    json_text = response.text
    rsp = loads(json_text)
    for book in rsp:
        print(book['title'], book['author'], book['category'])
