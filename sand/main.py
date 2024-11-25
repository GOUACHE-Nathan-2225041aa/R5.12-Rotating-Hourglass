from Matrix import *
from Display import *

matrix1 = Matrix()
matrix1.generate_hourglass(30, chance_of_content=0.8)
print(matrix1)
display = Display(pause_interval=0.5)

has_finished = False

while not has_finished:
    display.draw_frame(matrix1.matrix_content)
    has_finished = matrix1.update_matrix()

# Closes x seconds after the final result
plt.pause(5)
