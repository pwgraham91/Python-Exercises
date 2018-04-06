"""
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are
negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a
new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers
with absolute error of up to 10 ^ -4 are acceptable.

Input Format

The first line contains an integer, N, denoting the size of the array.
The second line contains N space-separated integers describing an array of numbers.

Output Format

You must print the following 3 lines:

A decimal representing of the fraction of positive numbers in the array.
A decimal representing of the fraction of negative numbers in the array.
A decimal representing of the fraction of zeroes in the array.
Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667
Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The respective fractions of positive numbers, negative numbers and zeroes are 3/6, 2/6 and 1/6 respectively.
"""

n = 6
arr = [-4, 3, -9, 0, 4, 1]

positive, negative, zeroes = 0, 0, 0

for i in arr:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zeroes += 1

print float(positive) / n
print float(negative) / n
print float(zeroes) / n
