import numpy as np
A,B = np.array([[2,-3,5],[-1,2,-3],[-3,-1,3]]),np.array([[20],[-11],[6]])
print(np.dot(np.linalg.inv(A), B))
