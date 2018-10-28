'''
Implement your own composition function.

Expected behaviour:

def inc(x):
 return x + 1

def square(x):
 return x**2

def double(x):
 return x*2

isd = composition(double, square, inc)
'''

def compose2(f1, f2):
    return lambda x: f1(f2(x))


def composition(*args):

    f = lambda x: x
    for fi in args:
        f = compose2(f, fi)
    return f


