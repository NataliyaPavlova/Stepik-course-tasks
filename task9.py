'''
Implement a SwitchDict class that inherits from the original dict class but has one additional method: petrify. Petrify will return an immutable version of the dict object on which the method was called. In order to do that, implement the immutable dictionary class and call it ImDict. ImDict should inerit from the dict class but an attempt to use any method that may mutate the original object of ImDict class should raise a type error with the following message: 'objects of type ImDict are immutable'
'''

class ImDict(dict):

    def err_msg(self, *args, **kwargs):
        raise TypeError('objects of type ImDict are immutable')

    clear = err_msg
    update = err_msg
    setdefault = err_msg
    pop = err_msg
    popitem = err_msg
    __setitem__ = err_msg
    __delitem__ = err_msg


class SwitchDict(dict):

    def petrify(self, *args, **kwargs):
        return ImDict(self)
