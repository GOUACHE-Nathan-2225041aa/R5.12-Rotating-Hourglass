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

        self.ax.set_xlim([0, len(matrix[0])])
        self.ax.set_ylim([0, len(matrix)])
        self.ax.set_aspect('equal')
        self.ax.autoscale(False)

        matrix = np.array(matrix)

        # Matrix's dimensions
        rows, cols = matrix.shape

        # Go through the matrix to draw the points
        # @todo : Rotate the matrix around itself
        # @todo : Translate everything in english
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] == 1:
                    color = "yo"
                elif matrix[i, j] == 2:
                    color = "ko"
                if matrix[i, j] in [1, 2]:
                    coordonnees_point = self.get_rotated_point([j, -i], angle)
                    plt.plot(coordonnees_point[0], coordonnees_point[1], color,
                             label=f'Value: {matrix[i, j]}' if i == 0 and j == 0 else "")

        plt.draw()
        plt.pause(self.pause_interval)

    def get_rotated_point(self, point, angle):

        angle = np.radians(angle)

        matrice_rotation = np.matrix([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])

        coordonnees_homogenes = np.matrix([[point[0]], [point[1]], [1]])

        coordonnes_homogenes_rotated = matrice_rotation @ coordonnees_homogenes

        return coordonnes_homogenes_rotated

    def set_angle(self, new_angle):
        self.angle = new_angle
