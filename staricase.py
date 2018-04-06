"""
Consider a staircase of size 4:

   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces.
The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.

Input Format

A single integer, n, denoting the size of the staircase.

Output Format

Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.

Sample Input

6
Sample Output

     #
    ##
   ###
  ####
 #####
######
Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of 6.
"""
import sys

n = 6
for a in xrange(n):
    for b in xrange(n):
        sys.stdout.write(str(b))
    print

for a in xrange(n):
    for b in xrange(n):
        if n - b <= a + 1:
            print '#',
        else:
            print ' ',
    print

