import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin


class Display:
    def __init__(self, pause_interval=0.00001, angle=0):
        self.pause_interval = pause_interval
        self.angle = angle
        self.fig, self.ax = plt.subplots()
        plt.ion()

    def draw_frame(self, matrix=[[0], [0]], angle=90):
        self.ax.clear()

        self.ax.set_xlim([-len(matrix[0]), len(matrix[0])])
        self.ax.set_ylim([-len(matrix), len(matrix)])
        self.ax.set_aspect('equal')
        self.ax.autoscale(False)

        matrix = np.array(matrix)

        # Matrix's dimensions
        rows, cols = matrix.shape

        # Go through the matrix to draw the points
        # @todo : Rotate the matrix around itself
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] == 1:
                    color = "yo"
                elif matrix[i, j] == 2:
                    color = "ko"
                if matrix[i, j] in [1, 2]:
                    point_to_rotate = [j - cols / 2, i - rows / 2]
                    point_coordinates = self.get_rotated_point(point_to_rotate, angle)
                    plt.plot(point_coordinates[0], point_coordinates[1], color,
                             label=f'Value: {matrix[i, j]}' if i == 0 and j == 0 else "")

        plt.draw()
        plt.pause(self.pause_interval)

    def get_rotated_point(self, point, angle):

        angle = np.radians(angle)

        matrix_rotation = np.matrix([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])

        homogeneous_coordinates = np.matrix([[point[0]], [point[1]], [1]])

        homogeneous_coordinates_rotated = matrix_rotation @ homogeneous_coordinates

        return homogeneous_coordinates_rotated
