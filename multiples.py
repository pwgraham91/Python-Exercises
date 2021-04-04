def run(multiples_list, until):
    sum_multiples = 0
    for until_num in range(1, until):
        print("until num {}".format(until_num))
        for multiple in multiples_list:
            if until_num % multiple == 0:
                sum_multiples += until_num
                print("summing {} {}".format(until_num, sum_multiples))
                break
    return sum_multiples

print(run([3, 5], 1000))