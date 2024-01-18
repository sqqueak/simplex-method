import numpy as np

def get_basic_variables_from_B_inverse(B_inverse, b):
    xB = []
    for row in B_inverse:
        res = sum([row[j] * bi for j, bi in enumerate(b)])
        xB.append([res])
    return xB

def get_basic_variables_from_B(B, b):
    return get_basic_variables_from_B_inverse(np.linalg.inv(B), b)

# not basic direction because it should have zeroes in it? then what is this called?
def get_basic_direction_from_B_inverse(B_inverse, Aj):
    dB = []
    for row in B_inverse:
        res = sum([row[j] * Aij for j, Aij in enumerate(Aj)])
        dB.append([-res])
    return dB

# missing components, doesn't work
def get_jth_reduced_cost(cj, cB, B_inverse, A):
    B_inverse = np.linalg.inv(B_inverse)

    # transpose cB
    # cB_transpose = [v[0] for v in cB]
    cB_transpose = cB

    # cB_transpose @ B_inverse @ A
    res1 = []
    for col in range(len(B_inverse)):
        res1.append(sum([cB_transpose[i] * B_inverse[i][col] for i in range(len(B_inverse[0]))]))
    
    res2 = []
    for col in range(len(A[0])):
        res2.append(sum([res1[i] * A[i][col] for i in range(len(res1))]))

    # cj - res2
    return [cj - res2[i] for i in range(len(res2))]

print(get_jth_reduced_cost(2,[1,1,0,0],[[1,1],[2,0]],[[1,1,1,1],[2,0,3,4]]))