import numpy as np

m1 = np.array([[-2,4],[1,0],[3,-1]])
m2 = np.array([[5,0],[-1,3]])
m3 = np.array([[2,1],[3,2]])

def mx_sum(m1:np.array, m2:np.array) -> np.array:
    return m1+m2

def mx_multiply(m1:np.array, m2:np.array) -> np.array:
    return np.dot(m1,m2) # must be i[j] == [i]j

def mx_transpose(m:np.array) -> np.array:
    return np.transpose(m1) # i -> j, j -> i

def mx_determinant(m:np.array) -> np.array:
    return np.linalg.det(m)

print(mx_sum(m2,m3))