'''
Rewrite the function below so there are no looping constructs (for, while) within the function's body. Make sure your function is pure.

def meanAge(records):
  ageRecs = 0
  ageTotal = 0

  for r in records:
    if 'age' in r.keys():
      ageRecs += 1
      ageTotal += r['age']

  if ageRecs:
   avg = ageTotal / ageRecs
   return avg
'''

import numpy as np

def meanAge(records):
   
    ages = [record['age'] for record in records if record and 'age' in record.keys()]
    if not ages:
        return None
    return np.mean(ages)


