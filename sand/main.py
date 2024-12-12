import time

from Matrix import *
from Display import *

pause_interval = 0.05

matrix1 = Matrix()
matrix1.generate_hourglass(10, chance_of_content=0.2)
display = Display(pause_interval)

angle = 0

angle += 90
matrix1.rotate_matrix()
while True:
    display.draw_frame(matrix1.matrix_content, angle)
    angle += 1
    if angle % 90 == 0:
        print(matrix1)
        while not matrix1.update_matrix():
            time.sleep(pause_interval)
            display.draw_frame(matrix1.matrix_content, angle)

        time.sleep(3)

        # La fonction pour bien faire tourner le sablier
        matrix1.rotate_matrix()
        angle -= 90
