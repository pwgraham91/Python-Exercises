"""
There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity).
The first kangaroo starts at location  and moves at a rate of  meters per jump. The second kangaroo starts at
location  and moves at a rate of  meters per jump. Given the starting locations and movement rates for each kangaroo,
can you determine if they'll ever land at the same location at the same time?

k1p v1 k2p v2
0  3  4  2

"""

from operator import itemgetter
k1p, v1, k2p, v2 = 0, 3, 4, 2

k1 = [k1p, v1]
k2 = [k2p, v2]

k1_spots = []
k2_spots = []

for i in range(10000):
    k1_spots.append(k1[0])
    k2_spots.append(k2[0])

    ks = [k1, k2]

    sorted_ks = sorted(ks, key=itemgetter(0))

    if sorted_ks[0][0] == sorted_ks[1][0]:
        print 'YES'
        break
    elif sorted_ks[0][1] > sorted_ks[1][1]:
        k1[0] = k1[0] + k1[1]
        k2[0] = k2[0] + k2[1]
    else:
        print 'NO'
        break
else:
    print 'NO'
