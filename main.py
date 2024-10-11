import random

from Matrix import *

matrix_size = 13
percentage_of_spawn = 0.1

matrix = []

for i in range(matrix_size):
    matrix.append([])
    for j in range(matrix_size):
        if random.random() < percentage_of_spawn:
            matrix[i].append(1)
        else:
            matrix[i].append(0)

matrix1 = Matrix(matrix)

print(matrix1)
matrix1.update_matrix()
