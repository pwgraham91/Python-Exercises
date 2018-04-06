"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can
change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you
must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height,
then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format

The first line contains three space-separated integers, , , and , describing the respective number of cylinders in
stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

The second line contains  space-separated integers describing the cylinder heights in stack .
The third line contains  space-separated integers describing the cylinder heights in stack .
The fourth line contains  space-separated integers describing the cylinder heights in stack .
Constraints

Output Format

Print a single integer denoting the maximum height at which all stacks will be of equal height.

Sample Input

5 3 4
3 2 1 1 1
4 3 2
1 1 4 1

Sample Output

5

"""

import collections
from operator import attrgetter


Stack = collections.namedtuple('Stack', 'stack sum name')

h1 = [1, 1, 1, 1, 2]
h2 = [3, 7]
h3 = [1, 3, 1]

h1_stack = Stack(h1, sum(h1), '1')
h2_stack = Stack(h2, sum(h2), '2')
h3_stack = Stack(h3, sum(h3), '3')

stacks = [h1_stack, h2_stack, h3_stack]

for i in range(max([len(stack.stack) for stack in stacks])):
    # check equality
    stack_sums = [_stack.sum for _stack in stacks]
    if min(stack_sums) == 0 or len(set(stack_sums)) == 1:
        print stacks[0].sum
        break

    stacks = sorted(stacks, key=attrgetter('sum'), reverse=True)

    long_stack = stacks[0]
    removed_number = long_stack.stack.pop(0)
    stacks[0] = long_stack._replace(sum=sum(long_stack.stack))
