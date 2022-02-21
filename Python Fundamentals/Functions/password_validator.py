def password_checker(password):
    first_rule = False
    second_rule = False
    third_rule = False
    digits = 0

    if 6 <= len(password) <= 10:
        first_rule = True
    else:
        first_rule = False

    for i, symbol in enumerate(password):

        if symbol.isdigit():
            second_rule = True
        elif symbol.isalpha():
            second_rule = True
        else:
            second_rule = False
            break

    for i, symbol in enumerate(password):
        if symbol.isdigit():
            digits += 1
            if digits >= 2:
                third_rule = True

    if not first_rule:
        print("Password must be between 6 and 10 characters")

    if not second_rule:
        print("Password must consist only of letters and digits")

    if not third_rule:
        print("Password must have at least 2 digits")

    if first_rule and second_rule and third_rule:
        print("Password is valid")


password_inp = input()
password_checker(password_inp)
