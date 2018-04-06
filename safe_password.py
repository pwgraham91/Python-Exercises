__author__ = 'petergraham'


def safe_password(data):
    one_digit = False
    upper = False
    lower = False
    for i in data:
        if i.isdigit():
            one_digit = True
        else:
            if i.isupper():
                upper = True
            else:
                lower = True

    if len(data) >= 10 and one_digit and upper and lower:
        return True
    else:
        return False
