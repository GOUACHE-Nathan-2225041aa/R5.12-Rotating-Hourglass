import random
import time

from Matrix import *

matrix_size = 50
percentage_of_spawn = 0.3

matrix = []

for i in range(matrix_size):
    matrix.append([])
    for j in range(matrix_size):
        if random.random() < percentage_of_spawn:
            matrix[i].append(0)
        else:
            matrix[i].append(" ")

matrix1 = Matrix(matrix)

print(matrix1)

inp = ""

while True:
    time.sleep(0.1)
    matrix1.update_matrix()
    print(matrix1)

# while inp != "stop":
#     inp = input()
#     matrix1.update_matrix()
#     print(matrix1)
