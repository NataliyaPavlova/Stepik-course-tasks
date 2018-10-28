'''
Rewrite the function below so it behaves as a pure function (Don't change anything outside the function's body).

def func(lst, n):
    for i in range(n):
        lst.append(i)
    return lst
'''

def func(lst, n):
     return lst+[i for i in range(n)]
   
