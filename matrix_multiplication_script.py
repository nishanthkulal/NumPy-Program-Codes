import numpy as np
n1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
n2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print("multiplication n1 * n2 ")
print(n1.dot(n2))
print("\n")
print("multiplication n2 * n1 ")
print(n2.dot(n1))
