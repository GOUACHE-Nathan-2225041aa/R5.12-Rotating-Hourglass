import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from Matrix import *
from Display import *

matrix1 = Matrix()
matrix1.generate_matrix(100)

display = Display()

has_finished = False

while not has_finished:
    display.draw_frame(matrix1.matrix_content)
    has_finished = matrix1.update_matrix()

# Closes x seconds after the final result
plt.pause(5)
