'''
Write a function to flatten a nested dictionary by joining the keys with a dot

Expected behaviour:

>>> flatten({'a': 1, 'b': {'1': 2, '2': 3}, 'c': 4})
{'a': 1, 'b.1': 2, 'b.2': 3, 'c': 4}
'''

def flatten(dct):
    d={}
    for k,v in dct.items():
        if not type(v)==type({}):
            d.update({k : v})
        else:
            d.update(flatten({'{}.{}'.format(k, a): b for a, b in v.items()}))
    return d
