'''
Implement a flip decorator that make so that decorated function takes all of its arguments in reverse order (no keyword arguments).
'''

def flip(f):
    def inner(*args):
        
        return f(*args[::-1])

    return inner

