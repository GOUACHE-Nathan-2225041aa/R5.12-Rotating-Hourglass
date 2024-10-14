import math


class Matrix:
    def __init__(self, matrix_content=[], content=0, space=" ", ):
        self.matrix_content = matrix_content
        self.content = content
        self.space = space

    def __str__(self):
        printable_matrix = ""
        for i in range(len(self.matrix_content)):
            for j in range(len(self.matrix_content[i])):
                printable_matrix += " " + str(self.matrix_content[i][j]) + " "
            printable_matrix += "\n"
        return printable_matrix

    def switch_points(self, x1, y1, x2, y2):
        temp = self.matrix_content[y1][x1]
        self.matrix_content[y1][x1] = self.matrix_content[y2][x2]
        self.matrix_content[y2][x2] = temp

    def update_line(self, y):
        for x in range(len(self.matrix_content[y])):
            if self.matrix_content[y][x] != self.content and self.content in self.matrix_content[y - 1]:
                best_distance = float("inf")
                for upper_x in range(len(self.matrix_content[y - 1])):
                    if self.matrix_content[y - 1][upper_x] == self.content:
                        distance_between_2_points = math.sqrt(abs(((x - upper_x) ** 2) + 1))
                        if distance_between_2_points < best_distance:
                            best_distance = distance_between_2_points
                            x_best_distance = upper_x
                self.switch_points(x_best_distance, y - 1, x, y)

    def update_matrix(self):
        # We check if every point can be updated
        for y in reversed(range(len(self.matrix_content))):
            self.update_line(y)
