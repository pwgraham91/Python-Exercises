import time


def run(list_seconds):
    sum_seconds = sum(list_seconds)
    hours = sum_seconds // 3600
    minutes = sum_seconds // 60 % 60
    seconds = sum_seconds % 60

    return "{}:{}:{}".format(hours, minutes, seconds)

print(run([37, 77, 35, 81, 33, 87]))
