import numpy as np
from random import randint

def sys_creator(lines:int, col:int, scale_range:int, xs_range:int) -> tuple:
    lin_system = []
    result_system = []
    xs = np.array([])

    # Creating the X values
    for _ in range(col):
        xs = np.append(xs,[randint((-1*xs_range), xs_range)])

    # Creating the Scalers
    for i in range(lines):
        total_line = 0
        lin_system.append([])

        for j in range(col):
            scalar = randint((-1*scale_range), scale_range)
            lin_system[i].append(scalar)
            total_line += scalar * xs[j]
        result_system.append([total_line])

    # list to np.array
    lin_system = np.array(lin_system)
    result_system = np.array(result_system)

    return (lin_system,result_system)
        
        

a, b = sys_creator(2,2,4,5)
