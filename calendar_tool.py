"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when
everyone is available.

To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple
of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:

[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

[(0, 1), (3, 8), (9, 12)]

https://www.interviewcake.com/question/python/merging-ranges
"""


def merge_ranges(schedules: list):
    """
    This is a brute force way of doing it which compares each range with previous ranges
    n^2
    """

    booked_ranges = []
    for event in schedules:
        event_start = event[0]
        event_end = event[1]

        changed = False

        remove_range_indices = []
        for i, _range in enumerate(booked_ranges):
            range_start = _range[0]
            range_end = _range[1]

            # if the event entirely encapsulates the booked range
            if event_start <= range_start and event_end >= range_end:
                remove_range_indices.append(i)
                continue

            num_matched = 0

            # if the event start is inside the range
            if event_start >= range_start and event_start <= range_end:
                num_matched += 1
                if event_end > range_end:
                    _range[1] = event_end
                    changed = True

            # if the event end is inside the range
            if event_end <= range_end and event_end >= range_start:
                num_matched += 1
                if event_start < range_start:
                    _range[0] = event_start
                    changed = True

            if num_matched == 2:
                # this fits in an existing range
                changed = True

        # if the event encapsulates the range, remove the range and add the event
        remove_range_indices.reverse()
        for i in remove_range_indices:
            del booked_ranges[i]

        if not changed:
            booked_ranges.append([event_start, event_end])

    booked_ranges.sort(key=lambda x: x[0])
    return booked_ranges


assert merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) == [[0, 1], [3, 8], [9, 12]]
assert merge_ranges([(3, 5), (0, 1), (9, 10), (4, 8), (10, 12)]) == [[0, 1], [3, 8], [9, 12]]
assert merge_ranges([(1, 2), (2, 3)]) == [[1, 3]]
assert merge_ranges([(1, 5), (2, 3)]) == [[1, 5]]
assert merge_ranges([(2, 3), (1, 5)]) == [[1, 5]]
assert merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]) == [[1, 10]]
assert merge_ranges([(2, 4), (7, 9), (1, 10)]) == [[1, 10]]


def sort_solution(schedules: list):
    """
    nlogn
    """
    schedules.sort(key=lambda x: (x[0], x[1]))

    booked_ranges = []
    for index, event in enumerate(schedules):
        event_start = event[0]
        event_end = event[1]

        if index == 0:
            booked_ranges.append((event_start, event_end))
        else:
            previous_range = booked_ranges[-1]
            previous_start = previous_range[0]
            previous_end = previous_range[1]

            # if the event start is inside the range
            if previous_start <= event_start <= previous_end:
                if event_end > previous_end:
                    booked_ranges[-1] = (previous_start, event_end)
            else:
                booked_ranges.append((event_start, event_end))

    return booked_ranges


assert sort_solution([(0, 3), (6, 10), (0, 1), (1, 5), (7, 9)]) == [(0, 5), (6, 10)]
assert sort_solution([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) == [(0, 1), (3, 8), (9, 12)]
assert sort_solution([(3, 5), (0, 1), (9, 10), (4, 8), (10, 12)]) == [(0, 1), (3, 8), (9, 12)]
assert sort_solution([(1, 2), (2, 3)]) == [(1, 3)]
assert sort_solution([(1, 5), (2, 3)]) == [(1, 5)]
assert sort_solution([(2, 3), (1, 5)]) == [(1, 5)]
assert sort_solution([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)]
assert sort_solution([(2, 4), (7, 9), (1, 10)]) == [(1, 10)]
