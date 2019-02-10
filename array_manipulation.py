"""
https://www.hackerrank.com/challenges/crush/problem

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros n = 10 . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->  1 2 3  4  5 6 7 8 9 10
        [0,0,0, 0, 0,0,0,0,0, 0]
        [3,3,3, 3, 3,0,0,0,0, 0]
        [3,3,3,10,10,7,7,7,0, 0]
        [3,3,3,10,10,8,8,8,1, 0]
The largest value is 10 after all operations are performed.


Input:
5 3
1 2 100
2 5 100
3 4 100

Output:
200

Explanation:
100 100  0   0   0
100 200 100 100 100
100 200 200 200 100

"""


def manipulate_array(n, queries):
    array = [0] * n

    for query in queries:
        for i in range(query[0], query[1] + 1):
            array[i - 1] += query[2]

    return max(array)


assert manipulate_array(5, [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]]) == 200
assert manipulate_array(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]) == 10
assert manipulate_array(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]) == 31
