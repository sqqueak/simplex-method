cost = input().split(" ")
constraints = []
variables = []

while w := input():
    words = w.split(" ")
    if words[-1] == '0' or words[-1] == "free":
        variables.append(words)
    else:
        constraints.append(words)

# redisplaying it to the user
print(f'you want to {cost[0]}imize the cost function {" ".join(cost[1:])}')
print(f'according to the following constraints')
for c in constraints:
    print(' '.join(c))
for v in variables:
    print(' '.join(v))
print()

# converting to dual problem
# 1. get b and c vectors
b = []
c = []
for cx in constraints:
    b.append(cx[-1])
for cx in cost:
    if cx not in {"min", "max", "+", "-"}:
        c.append(cx[:-2])

# print(c)
# print(b)

# 2. constructing A matrix and transpose
A = []
for cx in constraints:
    A.append([])
    for x in cx[:-1]:
        if x not in {"min", "max", "+", "-", "="}:
            A[-1].append(x[:-2])

# print(A)

# 3. constructing new cost function
new_cost = []
for i, x in enumerate(b):
    new_cost.append(f'{x}p{i + 1}')

# 4. constructing new constraints using transposed A
new_constraints = []
for col in range(len(A[0])):
    new_constraints.append([])
    for row in range(len(A)):
        new_constraints[-1].append(f'{A[row][col]}p{row + 1}')
        new_constraints[-1].append("+")
    new_constraints[-1].pop()
    if variables[col][1] == ">=":
        new_constraints[-1].append("<=")
    elif variables[col][1] == "<=":
        new_constraints[-1].append(">=")
    new_constraints[-1].append(c[col])
print("your corresponding dual problem is")
print(' '.join(new_cost))
print("according to the following constraints")
for cx in new_constraints:
    print(' '.join(cx))

# 5. getting new variable constraints
for i, cx in enumerate(constraints):
    if cx[-2] == "<=":
        print(f'p{i + 1} <= 0')
    elif cx[-2] == ">=":
        print(f'p{i + 1} >= 0')
    else:
        print(f'p{i + 1} free')