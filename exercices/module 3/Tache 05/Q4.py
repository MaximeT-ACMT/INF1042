def password_valid(password):

    has_number = False
    has_letter = False

    for character in password:

        if character in "Numbers 0 - 9":
            has_number = True

        if character in "Letters A - Z":
            has_letter = True

    if len(password) >= 8 and has_number and has_letter:
        return True
    else:
        return False