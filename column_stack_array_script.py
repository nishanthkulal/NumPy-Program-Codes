import numpy as mp

n1 = mp.array([10,20,30])
n2 = mp.array([40,50,60])

n3 = mp.column_stack((n1,n2))
print(n3)
