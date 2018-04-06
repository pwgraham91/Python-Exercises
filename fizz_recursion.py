def recur(number):
    if number % 2 == 0 and number % 3 == 0:
        print number, "fizz buzz"
    elif number % 2 == 0:
        print number, "fizz"
    elif number % 3 == 0:
        print number, "buzz"
    else:
        print number
    if number > 0:
        recur(number - 1)

recur(100)
