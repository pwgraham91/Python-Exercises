__author__ = 'petergraham'


def remove_unique_elements(data):
    test_data = data[:]
    print data, test_data
    for i in data:
        if data.count(i) == 1:
            test_data.remove(i)
    return test_data

print remove_unique_elements([1, 2, 3, 4, 5])