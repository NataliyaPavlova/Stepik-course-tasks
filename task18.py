'''
A Pythagorean triple is a set of three positive integers a,b,c such that  c2=a2+b2. Among those triples, there is a single one such that a+b+c=1000.

Implement a function findTheTriple that takes no arguments and returns this triple.

Try to analytically reduce the direct computations as much as possible and do not use loops.
'''

from itertools import combinations
from math import sqrt


def findTheTriple():
    # pool of (a,b) pairs. Use a,b < 500  and a + b > 500 due to triangle non-eq.
    cart = [pair for pair in combinations(range(500), r=2) if pair[0]+pair[1]>500]
    # looking for a result. Use c^2 = a^2 + b^2
    res = list(filter(lambda pair: pair[0]+pair[1]+sqrt(pair[0]**2+pair[1]**2)==1000, cart))
    final_set =[res[0][0], res[0][1], 1000-res[0][0]-res[0][1]]
    return set(final_set)

