import time

from Matrix import *
from Display import *

pause_interval = 0.01

matrix1 = Matrix()
matrix1.generate_hourglass(10, chance_of_content=0.2)
display = Display(pause_interval)

angle = 0

while True:
    display.draw_frame(matrix1.matrix_content, angle)
    angle += 1
    if angle % 90 == 0:
        while not matrix1.update_matrix():
            time.sleep(pause_interval)
            display.draw_frame(matrix1.matrix_content, angle)

        # La fonction pour bien faire tourner le sablier
        matrix1.rotate_matrix()
