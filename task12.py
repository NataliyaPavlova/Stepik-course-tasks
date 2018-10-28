'''
It's quite annoying to write a trivial wrapper around the inner function each time we write a decorator. Implement a makeDecorator decorator that works like that:

@makeDecorator
def introduce(f, *args, **kwargs):
  print(f.__name__)
  return f(*args, **kwargs)

# introduce is now a decorator

@introduce
def id(*whatever):
  return whatever


print(*(id(40, 2)))

>>> id
40 2
'''

def makeDecorator(func_dec):
    def inner(func):
        def ininner(*args):
            return func_dec(func, *args)
        ininner.__name__ = func.__name__
        ininner.__doc__ = func.__doc__

        return ininner

    return inner

