'''
Suppose we have a list of data x¯=[x0,x1,x2, ... ,xn]

Implement functions to calculate the sample mean (μ), variance (σ2), standard deviation (σ). The formulas are given below.
Don't use loops, use higher-order functions, composition, folds 
'''

import numpy as np

def sum(lst_):
    if not lst_: return 0
    return lst_[0] + sum(lst_[1:])

def mean(lst):
    return sum(lst)/len(lst)

def var(lst):
    m = mean(lst)
    add = [(x-m)**2 for x in lst]
    return sum(add)/len(lst)

def stdv(lst):
    return np.sqrt(var(lst))

