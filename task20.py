'''
Write a function sampleCount that receives some non-empty sample string and returns a function
 that takes a list of strings and returns the total number of occurences of the given sample within
  the strings of the given list.

The function that is returned from sampleCount should be implemented as a fold (that is, a body
 of the function should be a single reduce statement)'''

from toolz import reduce, partial
import string


def sampleCount(substring):
    condition = lambda x: x.count(substring)
    pred = lambda x, y: condition(x) + condition(y) if type(x) != int else x + condition(y)
    def f(func, lst):
        return reduce(func, lst)
    return partial(f, pred)

