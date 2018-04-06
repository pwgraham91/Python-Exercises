"""
Given 2 lines:
A: 5 6 7
B: 3 6 10

Compare by spots in line giving points to line A if it is higher and line B if it is higher and no points if they're
tied

Input:
5 6 7
3 6 10

Output:
1 1
"""

a = [5, 6, 7]
b = [3, 6, 10]
a_points = 0
b_points = 0

for i in range(len(a)):
    if a[i] > b[i]:
        a_points += 1
    elif a[i] < b[i]:
        b_points += 1

print(a_points)
print(b_points)
