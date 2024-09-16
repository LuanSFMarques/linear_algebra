matrix_a = [
    [1,3,5],
    [2,4,6]
]

matrix_b = [
    [-4,-3,-2],
    [2,4,6]
]

matrix_c = [
    [0],
    [1]
]

def sum_matrix(m1:list,m2:list) -> list:
    if equalsizemx(m1,m2):
        new_list = []
        for i in range(len(m1)):
            new_list.append([])
            for j in range(len(m1[i])):
                new_list[i].append(m1[i][j]+m2[i][j])
        return new_list
    else:
        return None
    
def mult_matrix(matrix:list,num:float) -> list:
    new_list = []
    for i in range(len(matrix)):
        new_list.append([])
        for j in range(len(matrix[i])):
            new_list[i].append((matrix[i][j]*num))
    return new_list

def equalsizemx(m1:list,m2:list) -> bool:
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            try:
                m1[i][j] = m1[i][j]
                m2[i][j] = m2[i][j]
            except IndexError:
                return False
    return True
    
#print(equalsizemx(matrix_a,matrix_b))
#print(sum_matrix(matrix_a,matrix_b))
print(mult_matrix(matrix_a,2))