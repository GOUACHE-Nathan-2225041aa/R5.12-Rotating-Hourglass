import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Display:
    def __init__(self, color_map=ListedColormap(['k', 'b'])):
        self.color_map = color_map
        self.fig = plt.figure()

    def draw_frame(self, matrix=[[0],[0]], pause_interval=0.00001):
        plt.clf()
        ax = self.fig.add_subplot(111)
        ax.matshow(matrix, cmap=self.color_map)
        plt.draw()
        plt.pause(pause_interval)
