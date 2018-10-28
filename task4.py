'''
Implement a recursive exponentiation algorithm based on the following principle:

If we want to raise some number a to the  n'th power, where  n is a positive integer, then:

if  n is even, we may represent the result of  an as an/2⋅an/2 
if n is odd then the result is a⋅an−1 and n−1  is guaranteed to be even
Figure out a suitable edge-case.

Write a function quickPower(base, power) ﻿that is based on that  algorithm.

'''


def quickPower(base, power):
    if power==0: return 1
    elif power%2==0: return quickPower(base*base, power/2)
    else: return base*quickPower(base, power-1)

