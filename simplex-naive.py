import utils.calculate

A = [[1,2,2,1,0,0],[2,1,2,0,1,0],[2,2,1,0,0,1]]
B = [[1,0,0],[0,1,0],[0,0,1]]
b = [20, 20, 20]
basic_indices = (3,4,5)
c = [-10,-12,12,0,0,0]

# print(utils.calculate.get_new_point(Ax,Bx,bx,basic_indicesx, 3))

# Bx = [[1,1],[0,3]]
# basic_indicesx = (2,3)

# print(utils.calculate.get_new_point(Ax,Bx,bx,basic_indicesx, 1))

# calculating wrong
B, basic_indices = utils.calculate.iterate(A, B, b, basic_indices, c)
print(basic_indices)
B, basic_indices = utils.calculate.iterate(A, B, b, basic_indices, c)
print(basic_indices)
