def run(upper_limit):
    last_one = 1
    last_two = 2
    sum_even = 2
    while last_one + last_two < upper_limit:
        new = last_one + last_two
        if new % 2 == 0:
            sum_even += new
        last_one = last_two
        last_two = new
        print("{} {}".format(new, sum_even))
    return sum_even


print(run(4000000))
