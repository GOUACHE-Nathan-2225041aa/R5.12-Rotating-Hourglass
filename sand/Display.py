import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


class Display:
    def __init__(self, pause_interval=0.00001, angle=0):
        self.fig = plt.figure()
        self.pause_interval = pause_interval
        self.angle = angle

    def draw_frame(self, matrix=[[0],[0]]):

        matrix = np.array(matrix)

        # Matrix's dimensions
        rows, cols = matrix.shape

        # Go through the matrix to draw the points
        # @todo : Rotate the matrix
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] == 1:
                    color = "yo"
                elif matrix[i, j] == 2:
                    color = "ko"
                else:
                    color = "wo"
                plt.plot(j*0.1, -i*0.1, color,
                         label=f'Value: {matrix[i, j]}' if i == 0 and j == 0 else "")  # -i pour inverser les axes

        plt.draw()
        plt.pause(self.pause_interval)

    def set_angle(self, new_angle):
        self.angle = new_angle
