"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

Sample Input:
8
UDDDUDUU

Sample Output:
1
"""


def count_valleys(steps):
    current_elevation = 0
    num_valleys = 0

    for step in steps:
        previous_elevation = current_elevation
        current_elevation += 1 if step == 'U' else -1
        if current_elevation > previous_elevation and current_elevation == 0:
            num_valleys += 1

    return num_valleys


assert count_valleys('DDUUUUDD') == 1
assert count_valleys('UDDDUDUU') == 1
