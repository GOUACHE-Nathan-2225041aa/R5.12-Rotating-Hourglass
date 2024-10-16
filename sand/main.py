import random
import time
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from Matrix import *

# Randomization and size of the matrix
matrix_size = 21
percentage_of_spawn = 0.2
# Contents
nothing = 1
something = 0
# Init of the matrix
matrix = []

# Filling the matrix
for i in range(matrix_size):
    matrix.append([])
    for j in range(matrix_size):
        if random.random() < percentage_of_spawn:
            matrix[i].append(something)
        else:
            matrix[i].append(nothing)

# Creating the object from the Matrix class
matrix1 = Matrix(matrix, something, nothing)

# Displaying the Matrix
fig = plt.figure()
ax = fig.add_subplot(111)
ax.matshow(matrix1.matrix_content)

while True:
    matrix1.update_matrix()
    ax = fig.add_subplot(111)
    ax.matshow(matrix1.matrix_content, custom_color_map)
    plt.draw()
    plt.pause(0.0001)
