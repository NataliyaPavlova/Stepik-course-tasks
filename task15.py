'''
Recall the Church numerals

zero = lambda f: lambda x: x

one = lambda f: lambda x: f(x)

two = lambda f: lambda x: f(f(x))

three = lambda f: lambda x: f(f(f(x)))
 
And the Church booleans

true = lambda x: lambda y: x

false = lambda x: lambda y: y

You're asked to construct the isZero predicate that takes a Church numeral as its input and returns a Church boolean value: true if this numeral is the zero numeral and false otherwise.


To do that, think of what distinguishes the zero numeral from any other one. Try to construct a function that exploits this distinction to return false if  the given numeral is any other than zero and to return true otherwise.
'''

def isZero(numeral):
    false_ = lambda x: false
    return numeral(false_)(true)
