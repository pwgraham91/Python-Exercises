"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

Input:
9
10 20 20 10 10 30 50 10 20

Output:
3
"""


def get_num_match_socks(socks):
    unmatched_socks = {}
    num_matched_socks = 0

    for i in socks:
        if unmatched_socks.get(i):
            del unmatched_socks[i]
            num_matched_socks += 1
        else:
            unmatched_socks[i] = 1

    return num_matched_socks


assert get_num_match_socks([10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
