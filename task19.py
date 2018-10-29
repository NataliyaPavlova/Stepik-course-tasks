'''
1) Implement the maximum function that takes an iterable containing numbers and returns it's maximal element or minus infinity if the iterable is empty. Define this function in terms of reduce.
2)Define the following functions:

myAll takes a predicate and a sequence, returns True if all the elements of the sequence satisfy the given predicate and False otherwise

myAny  takes a predicate and a sequence, returns True if there is an element of the sequence that satisfies the given predicate

Also, implement a function elem that takes an element and returns another function. This last function takes a sequence and returns True if the given element is in this sequence and False otherwise. Implement the elem function in terms of myAll or  myAny.


'''

from functools import partial, reduce
from math import inf

def maximum(iter):
    bigger = lambda x,y: x if x >= y else y
    return reduce(lambda x,y: bigger(x,y), iter, -inf)


def myAll(predicate, seq):
    f = lambda x,y: predicate(x) and predicate(y) if type(x)!=bool else x and predicate(y)
    return reduce(f, seq)

def myAny(predicate, seq):
    f = lambda x, y: predicate(x) or predicate(y) if type(x)!=bool else x or predicate(y)
    return reduce(f, seq)

def elem(n):
    return partial(myAny, lambda x: x==n)

