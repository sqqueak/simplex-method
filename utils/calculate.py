import numpy as np
import time

def get_basic_variables_from_B_inverse(B_inverse, b):
    return B_inverse @ b

def get_basic_variables_from_B(B, b):
    return get_basic_variables_from_B_inverse(np.linalg.inv(B), b)

# not basic direction because it should have zeroes in it? then what is this called?
def get_basic_direction_from_B_inverse(B_inverse, Aj):
    return B_inverse @ Aj



# we will specify matrix and its basis, and its basic columns
A = [[1,1,1,1],[2,0,3,4]]
B = [[1,1],[2,0]]
b = [2,2]
basic_indices = (0,1)

def get_solution_for_basis_B(A, B, b, basic_indices):
    x = [0 for _ in range(len(A[0]))]
    xB = get_basic_variables_from_B(B, b)
    for i, val in enumerate(basic_indices):
        x[val] = xB[i]
    return x

def get_jth_basic_direction(A, j, B, basic_indices):
    j -= 1
    d = [0 for _ in range(len(A[0]))]
    Aj = [A[v][j] for v in range(len(A))]
    dB = get_basic_direction_from_B_inverse(np.linalg.inv(B), Aj) 
    for i, val in enumerate(basic_indices):
        d[val] = -dB[i]
    d[j] = 1
    return d

# forgot cj?
def get_reduced_cost(c, B, A, b, basic_indices, j):
    d = get_jth_basic_direction(A, j, B, basic_indices)
    cB = [d[i] * c[i] for i in range(len(d)) if d[i] != 0]
    return sum(cB)

def get_max_theta_star(x, d):
    return max([-x[i]/d[i] if d[i] != 0 else 0 for i in range(len(x))])

def get_new_point():
    x = get_solution_for_basis_B(A,B,b,basic_indices)
    d = get_jth_basic_direction(A, 3, B, basic_indices)
    theta_star = get_max_theta_star(x, d)
    return [x[i] + theta_star * d[i] for i in range(len(x))]

print(get_new_point())