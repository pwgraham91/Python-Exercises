"""
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes jumps while the second takes .

Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

Input:
7
0 0 1 0 0 1 0

Output: 4

Input:
6
0 0 0 0 1 0

Output:
3

"""


def jump_clouds(len_clouds, clouds):
    current_cloud = 0
    num_jumps = 0

    while True:
        if len_clouds > current_cloud + 2 and clouds[current_cloud + 2] == 0:
            num_jumps += 1
            current_cloud += 2
        elif len_clouds > current_cloud + 1 and clouds[current_cloud + 1] == 0:
            num_jumps += 1
            current_cloud += 1
        else:
            return num_jumps


assert jump_clouds(7, [0, 0, 1, 0, 0, 1, 0]) == 4
assert jump_clouds(6, [0, 0, 0, 0, 1, 0]) == 3
