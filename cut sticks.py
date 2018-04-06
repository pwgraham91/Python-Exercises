"""
Given a list of the length of sticks, the sticks are cut by the length of the smallest stick. Sticks with length 0 or
less are discarded. Print the number of sticks remaining after each cut

6
5 4 4 2 2 8
"""

arr = [1, 2, 3, 4, 3, 3, 2, 1]

arr.sort()

for i in xrange(len(arr)):
    print len(arr)
    shortest = arr[0]
    arr = [num - shortest for num in arr if (num - shortest) > 0]
    length = len(arr)

    if length == 0:
        break
