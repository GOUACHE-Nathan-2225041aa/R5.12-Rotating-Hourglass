import time

from Matrix import *
from Display import *

matrix1 = Matrix()
matrix1.generate_hourglass(15, chance_of_content=0.2)
display = Display(pause_interval=0.3)

while True:
    display.draw_frame(matrix1.matrix_content)
    matrix1.update_matrix()
    print(matrix1)
    break