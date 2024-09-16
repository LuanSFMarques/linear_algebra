import numpy as np

# Ax = b
# x = b/A
# x = b * A^(-1)

A = np.array([
    [3,-1],
    [2,3]
    ])

B = np.array([
    [7],
    [1]
    ])

X = np.dot(np.linalg.inv(A), B)

#print(X)
