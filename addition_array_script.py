import numpy as np 

n1 = np.array([10,20])
n2 = np.array([30,40])
print("total sum")
print( np.sum([n1,n2]))
print("column sum")
print(np.sum([n1,n2],axis=0))
print("row sum")
print(np.sum([n1,n2],axis=1))
