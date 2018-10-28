'''
Write a function deepReverse to reverse elements of a nested list with an arbitrary level of nesting.

Expected behaviour:

>>> deepReverse([[1, 2], [3, [4, 5]], 6])
[6, [[5, 4], 3], [2, 1]]
'''

def deepReverse(l):
    return list(map(deepReverse, l[::-1])) if isinstance(l, list) else l
