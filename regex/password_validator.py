def validate_password(string):
    """
    1. Validates the password for Mimimum 8 characters and Maximum 15 characters
    2. Password should have atelast 2 uppercase characters, 2 lowercase characters,
        2 digits, 2 special characters
    3. Password should not contain spaces
    """
    MIN_LEN = 8
    MAX_LEN = 15
    u_case = findall("[A-Z]", string)
    l_case = findall("[a-z]", string)
    digits = findall("[0-9]", string)
    special = findall("[^A-Za-z0-9]", string)
    spaces = findall(r"\s", string)

     # check if the min and max length of the password
    if MIN_LEN < len(string) > MAX_LEN:
        raise ValueError(f'Minimum length of password must be {MIN_LEN} and max length must be {MAX_LEN}')

    # validate the password for spaces
    if spaces:
        raise ValueError("spaces are not allowed")

    # validation for minimum character requirements
    if len(u_case) and len(l_case) and len(digits) and len(special) >= 2:
        return "Password validated successfully"
    raise ValueError("Password does not meet minimum password requirement")
