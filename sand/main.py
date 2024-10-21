from Matrix import *
from Display import *

matrix1 = Matrix()
matrix1.generate_matrix(10, chance_of_content=0.6)

matrix1.matrix_content[3] = [0, 0, 2, 0, 0, 0, 0, 2, 0, 0]
matrix1.matrix_content[4] = [0, 0, 2, 0, 0, 0, 0, 2, 0, 0]
matrix1.matrix_content[5] = [0, 0, 2, 2, 2, 2, 2, 2, 0, 0]

display = Display(pause_interval=1)

has_finished = False

while not has_finished:
    display.draw_frame(matrix1.matrix_content)
    has_finished = matrix1.update_matrix()

# Closes x seconds after the final result
plt.pause(5)
