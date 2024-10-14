import random

from Matrix import *

matrix_size = 7
percentage_of_spawn = 0.2

nothing = 0
something = 1

matrix = []

for i in range(matrix_size):
    matrix.append([])
    for j in range(matrix_size):
        if random.random() < percentage_of_spawn:
            matrix[i].append(something)
        else:
            matrix[i].append(nothing)

matrix1 = Matrix(matrix, something, nothing)

print(matrix1)

inp = ""

# while True:
#     time.sleep(0.1)
#     matrix1.update_matrix()
#     print(matrix1)
#
while inp != "stop":
    inp = input()
    matrix1.update_matrix()
    print(matrix1.matrix_content)
    print(matrix1)
