'''
Write a recursive procedure that, given an amount and values available,  returns a number of ways in which this amount can be composed using these values. Use the following principle.

Looking at some particular value from the pool, we may define the number of  ways to compose the given amount as the sum of:
 the number of ways to compose the amount without using this value
the number of ways to compose (amount - value) with using this value
'''

def makeAmount(val, set_vals):
    if val==0:
        return 1
    if val < 0 or not set_vals:
        return 0
    else:
        return makeAmount(val, set_vals[1:]) + makeAmount(val-set_vals[0], set_vals)


