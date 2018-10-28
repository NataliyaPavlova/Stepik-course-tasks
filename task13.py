'''
Recall the Church numerals

zero = lambda f: lambda x: x

one = lambda f: lambda x: f(x)

two = lambda f: lambda x: f(f(x))

three = lambda f: lambda x: f(f(f(x)))
 
You are asked to implement the power function that takes two numerals and produces the resulting numeral. 
'''

pow = lambda b: lambda e: e(b)

