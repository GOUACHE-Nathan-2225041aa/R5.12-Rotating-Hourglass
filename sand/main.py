import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from Matrix import *
from Display import *

# Randomization and size of the matrix
matrix_size = 100
percentage_of_spawn = 0.25
# Contents
nothing = 0
something = 1
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

# Customizing the colors of the matrix
custom_colors_map = ListedColormap(['k', 'b'])

# Creating the object from the Matrix class
matrix1 = Matrix(matrix, something, nothing)

display = Display(custom_colors_map)

has_finished = False

while not has_finished:
    has_finished = matrix1.update_matrix()
    display.draw_frame(matrix1.matrix_content)

# Closes x seconds after the final result
plt.pause(5)
