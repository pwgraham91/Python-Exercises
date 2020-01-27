def solve():
    # if this is wrong try +1 or -1. the range rules could be weird
    good_nums = 0
    for i in range(138241, 674034):
        if is_good_num(i):
            good_nums += 1

    return good_nums


def is_good_num(num):
    stringified_num = str(num)
    has_double = False
    for i in range(len(stringified_num)):
        if i == 0:
            continue

        stringified = stringified_num[i]
        previous_num = stringified_num[i - 1]
        if previous_num == stringified:
            try:
                double_previous = stringified_num[i - 2]
            except IndexError:
                double_previous = None
            try:
                forward = stringified_num[i + 1]
            except IndexError:
                forward = None
            if not (double_previous == stringified or forward == stringified):
                has_double = True
        if int(stringified) < int(previous_num):
            return False

    return has_double

print(is_good_num(112233))
print(is_good_num(123444))
print(is_good_num(111122))

print(solve())

