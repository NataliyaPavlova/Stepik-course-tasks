'''
Make a bucket(<...>) decorator that works like that:

@bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one = 1, two = 2, three = 3)
def id(x):
  return x

>>> id(42)
((1, 2, 3, [1, 2, 3], 'one', 'two', 'three'), {'two': 2, 'one': 1, 'three': 3}, 42)



@bucket()
def id2(x):
  return x

>>> id2(42)
((), {}, 42)
'''

def bucket(*args, **kwargs):
    def wrap(f):
        def inner(f):
            
            return (args, kwargs, f)
        return inner
    return wrap

