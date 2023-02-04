from csv import reader

def _total():
    total = 0.00
    with open("../data_files/employees3.csv") as f:
        rows = reader(f)
        headers = next(rows)        # skipping headers
        for row in rows:
            try:
                total = total + int(row[2])
            except ValueError:
                # Recovery step
                print(f"Got some bad record: {row}")
                continue
    return total

names = ['apple', 'google', 'yahoo', 'yahoo', 'apple', 'apple']
{'apple': 3, 'google': 1}

count = { }
for name in names:
    try:
        count[name] = count[name] + 1
    except KeyError:
        count[name] = 1
        continue

def process(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 0
    result = result + 20
    result = result * 8
    return result

def process(n1, n2):
    try:
        result = n1 / n2
    except (ZeroDivisionError, TypeError):
        return 0
    result = result + 20
    result = result * 8
    return result

def factorial(number):
    if isinstance(number, str):
        raise TypeError("Strings are not allowed")
    if isinstance(number, float):
        raise TypeError("Floating point numbers are not allowed")
    if number < 0:
        raise ValueError("Number cannot be negative")
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


def func():
    try:
        print("Executing try block")
        a = 1 / 0
    except Exception:
        print("Executing except block")
    else:
        # else block gets executed only if there is no
        # exception in try block
        print("Executing else block")
    finally:
        # gets executed no matter what happens in try, except and else block
        # clean up actions like closing file, database connection etc
        print("Executing finally block")

def func():
    try:
        return 1
    except Exception:
        return 2
    else:
        return 3
    finally:
        print("FINALLY")


def func():
    try:
        print('hello world')
    except Exception:
        return 2
    else:
        return 3
    finally:
        return 4

# writing own custom exception
class InsufficientFundsError(Exception):
    pass

class AuthError(Exception):
    pass

def withdraw(amount):
    if amount > 1000:
        raise InsufficientFundsError("STOP")
    return amount

def login(username, password):
    if username == "admin" and password == "Password123":
        print("Login success")
    else:
        raise AuthError("Invalid credentials")


def add(a, b):
    return a + b

def div(a, b):
    return a / b

def spam(name):
    return name[10]

class CallbackError(Exception):
    pass

# exception chaining
def delay(seconds, func, *args, **kwargs):
    from time import sleep
    sleep(seconds)
    try:
        return func(*args, **kwargs)        # add(1, '2')
    except Exception as e:
        raise CallbackError from e
