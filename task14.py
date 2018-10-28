'''
Recall the church booleans.

true = lambda x: lambda y: x

false = lambda x: lambda y: y
 
Also, here's an and gate

und = lambda b1: lambda b2: b1(b2)(b1)

Following similar logic, construct an or gate. 
'''

orr = lambda b1: lambda b2: b1(b1)(b2)

