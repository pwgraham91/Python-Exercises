"""
A sequence of integers is called a zigzag sequence if each of its elements is either strictly less than all its
neighbors or strictly greater than all its neighbors. For example, the sequence 4 2 3 1 5 3 is a zigzag,
but 7 3 5 5 2 and 3 8 6 4 5 aren't. Sequence of length 1 is also a zigzag.

For a given array of integers return the length of its longest contiguous sub-array that is a zigzag sequence.

Example

For a = [9, 8, 8, 5, 3, 5, 3, 2, 8, 6], the output should be
zigzag(a) = 4.

The longest zigzag sub-arrays are [5, 3, 5, 3] and [3, 2, 8, 6] and they both have length 4.

For a = [4, 4], the output should be
zigzag(a) = 1.

The longest zigzag sub-array is [4] - it has only one element, which is strictly greater than all its neighbors (there are none of them).

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Guaranteed constraints:
2 ≤ a.length ≤ 25,
0 ≤ a[i] ≤ 100.

[output] integer
"""


def solve(array):
    if len(array) == 1:
        return 1

    next_greater = array[0] < array[1]

    streaks = []

    current_streak = 1
    for i, obj in enumerate(array):
        # don't run on the last one
        if len(array) == i + 1:
            break
        current_greater = array[i] < array[i + 1]

        if current_greater != next_greater or array[i] == array[i + 1]:
            # if the streak is broken...
            streaks.append(current_streak)
            if array[i] != array[i + 1]:
                # start the next streak with 2 if the previous streak was broken but the start of the next one is good
                current_streak = 2
            else:
                current_streak = 1

            try:
                # this will get flipped at the end of the loop
                next_greater = array[i] < array[i + 1]
            except IndexError:
                pass

        else:
            current_streak += 1

        next_greater = not next_greater

    streaks.append(current_streak)

    return max(streaks)


assert solve([9, 8, 8, 5, 3, 5, 3, 2, 8, 6]) == 4
assert solve([4, 4]) == 1
