from Matrix import *
from Display import *

matrix1 = Matrix()
matrix1.generate_hourglass(50, chance_of_content=0.3)
display = Display(pause_interval=0.05)

while True:
    display.draw_frame(matrix1.matrix_content)
    if matrix1.update_matrix():
        matrix1.matrix_content.reverse()

# Closes x seconds after the final result
plt.pause(5)
