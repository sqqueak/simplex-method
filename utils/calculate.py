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

def get_solution_for_basis_B(A, B, b, basic_indices):
    x = [0 for _ in range(len(A[0]))]
    xB = get_basic_variables_from_B(B, b)
    for i, val in enumerate(basic_indices):
        x[val] = xB[i]
    return x

def get_jth_basic_direction(A, j, B, basic_indices):
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
    cB = [d[i] * c[i] for i in range(len(d))]
    return sum([c[i] - cB[i] for i in range(len(c))])

def get_max_theta_star(x, d):
    return max([-x[i]/d[i] if d[i] != 0 else 0 for i in range(len(x))])

def get_new_point(x, d, theta_star):
    return [x[i] + theta_star * d[i] for i in range(len(x))]

def iterate(A, B, b, basic_indices, c):
    x = get_solution_for_basis_B(A,B,b,basic_indices)
    print(x)
    d = None

    # picking jth basic direction
    for jx in range(len(x)):
        cost = get_reduced_cost(c, B, A, b, basic_indices, jx)
        if cost < 0:
            print(cost)
            d = get_jth_basic_direction(A, jx, B, basic_indices)
            break

    print(d)

    if d == None:
        return ()

    theta_star = get_max_theta_star(x, d)
    print(theta_star)
    new_point = get_new_point(x, d, theta_star)

    basic_indices_new = []
    for i in range(len(new_point)):
        if new_point[i] != 0:
            basic_indices_new.append(i)

    basis_new = [[A[j][i] for j in range(len(A))] for i in basic_indices_new]
    print(new_point)
    return (basis_new, tuple(basic_indices_new))