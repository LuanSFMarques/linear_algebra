import numpy as np

m1 = np.array([[-2,4],[1,0],[3,-1]])
m2 = np.array([[5,0],[-1,3]])
m3 = np.array([[2,1],[3,2]])

def sum(m1:np.array, m2:np.array) -> np.array:
    return m1+m2

def multiply(m1:np.array, m2:np.array) -> np.array:
    return np.dot(m1,m2) # must be i[j] == [i]j

def transpose(m1:np.array) -> np.array:
    return np.transpose(m1)

print(sum(m2,m3))