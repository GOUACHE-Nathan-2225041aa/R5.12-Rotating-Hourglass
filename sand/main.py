import time

from Matrix import *
from Display import *

matrix1 = Matrix()
matrix1.generate_hourglass(11, chance_of_content=random.random())
display = Display(pause_interval=0.1)

while True:
    display.draw_frame(matrix1.matrix_content)
    time.sleep(5)
    matrix1.rotate_matrix(90)
    # if matrix1.update_matrix():
    #     time.sleep(1)
    #     matrix1.rotateMatrix()