import numpy as np

m1= np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
x = np.array([
    [1,0,0],
    [0,1,0],
    [4,0,1]
])
r = np.array([
    [1,2,3],
    [7,8,9],
    [4,5,6]
])

print(m1)
print(np.dot(x,m1))