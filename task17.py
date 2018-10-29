'''
Suppose we have two lists containing numerical data that both have the same length:

x¯=[x1,x2, ... ,xn],y¯=[y1,y2, ... ,yn]

Implement a function that takes such two lists and returns the correlation coefficient. 
Don't use loops, use higher-order functions, composition, folds 
'''

from functools import reduce
from math import sqrt

def sum(lst):
    return reduce(lambda x, y: x+y, lst)

def mean(lst):
    return sum(lst)/len(lst)

def var(lst):
    m = mean(lst)
    add = [(x-m)**2 for x in lst]
    return sum(add)/len(lst)

def crlt(x,y):
    mu_x, mu_y = mean(x), mean(y)
    n = len(x)
    numerator = sum(list(map(lambda a: a[0]*a[1]-mu_x*mu_y, zip(x,y))))/n
    divider = sqrt(var(x)*var(y))
    return numerator/divider



