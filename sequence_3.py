# Given [1, 4, 10, 19, 31], write a function that computes the sequence to a desired length.


def poly(length):
    list = [1]
    counter = 3
    for i in range(length):
        list.append(list[-1] + counter)
        counter += 3
    return list
