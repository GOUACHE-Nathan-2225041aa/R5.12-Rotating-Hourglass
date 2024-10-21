import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Display:
    def __init__(self, color_map=ListedColormap(['k', 'b', 'w']), pause_interval=0.00001):
        self.color_map = color_map
        self.fig = plt.figure()
        self.pause_interval = pause_interval

    def draw_frame(self, matrix=[[0],[0]]):
        plt.clf()
        ax = self.fig.add_subplot(111)
        ax.matshow(matrix, cmap=self.color_map)
        plt.draw()
        plt.pause(self.pause_interval)
