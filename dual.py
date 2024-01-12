from utils.parse import *

pr = LinearProgram(get_equation_from_string(input()), [], [])
while w := input():
    e = get_equation_from_string(w)
    # print(e.b)
    if e.b == 0: # or its a string equal to "free"
        pr.variables.append(e)
    else:
        pr.constraints.append(e)
print(f'primal\n{pr}')

du = LinearProgram(None, [], [])



# converting to dual problem
# 1. get A matrix, b and c vectors
A = [cx.a for cx in pr.constraints]
b = [cx.b for cx in pr.constraints]
c = pr.cost.a

# 2. constructing new cost function
new_cost = []
for i, x in enumerate(b):
    new_cost.append(f'{x}p{i + 1}')

print()
print("dual")
print(' '.join(new_cost))

# 4. constructing new constraints using transposed A
new_constraints = []
for col in range(len(A[0])):
    new_constraints.append([])
    for row in range(len(A)):
        new_constraints[-1].append(f'{A[row][col]}p{row + 1}')
        new_constraints[-1].append("+")
    new_constraints[-1].pop()

    if pr.variables[col].sign == ">=":
        new_constraints[-1].append("<=")
    elif pr.variables[col].sign == "<=":
        new_constraints[-1].append(">=")
    
    new_constraints[-1].append(c[col])

for cx in new_constraints:
    print(' '.join([str(s) for s in cx]))

# 5. getting new variable constraints
for i, cx in enumerate(pr.constraints):
    if cx.sign == "<=":
        print(f'p{i + 1} <= 0')
    elif cx.sign == ">=":
        print(f'p{i + 1} >= 0')
    else:
        print(f'p{i + 1} free')