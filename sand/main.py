import time

from Matrix import *
from Display import *

matrix1 = Matrix()
matrix1.generate_hourglass(10, chance_of_content=0.2)
display = Display(pause_interval=0.01)

angle = 0

while True:
    display.draw_frame(matrix1.matrix_content, angle)
    angle += 1
    if matrix1.update_matrix() :
        matrix1.matrix_content.reverse()
