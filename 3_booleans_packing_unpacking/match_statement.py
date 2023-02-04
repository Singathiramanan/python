"""
A match statement takes an expression and compares its value to successive patterns
given as one or more case blocks. This is superficially similar to a switch
statement in C, Java or JavaScript (and many other languages).
"""

def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 404:
            return "not found"
        case 418:
            return "hello world"
        case _:
            return "something went wrong"
