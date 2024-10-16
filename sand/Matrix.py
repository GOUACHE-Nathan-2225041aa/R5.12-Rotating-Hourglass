import math


class Matrix:
    def __init__(self, matrix_content=[], content=0, space=" ", ):
        self.matrix_content = matrix_content
        self.content = content
        self.space = space

    # A user-friendly way to display the matrix's content
    def __str__(self):
        printable_matrix = ""
        for i in range(len(self.matrix_content)):
            for j in range(len(self.matrix_content[i])):
                printable_matrix += " " + str(self.matrix_content[i][j]) + " "
            printable_matrix += "\n"
        return printable_matrix

    # Switch 2 points together
    def switch_points(self, x1, y1, x2, y2):
        temp = self.matrix_content[y1][x1]
        self.matrix_content[y1][x1] = self.matrix_content[y2][x2]
        self.matrix_content[y2][x2] = temp

    def update_line(self, y):
        # Go through the y row
        for x in range(len(self.matrix_content[y])):
            if (self.matrix_content[y][x] == self.content and y != len(self.matrix_content) - 1
                    and self.matrix_content[y + 1].count(self.content) != len(self.matrix_content[y + 1])):
                best_distance = float("inf")
                x_best_distance = -1
                for upper_x in range(len(self.matrix_content[y + 1])):
                    if self.matrix_content[y + 1][upper_x] != self.content:
                        # ON FAIT DES MATHS
                        distance_between_2_points = math.sqrt(abs(((x - upper_x) ** 2) + 1))
                        if distance_between_2_points < best_distance:
                            best_distance = distance_between_2_points
                            x_best_distance = upper_x
                if x_best_distance != -1:
                    self.switch_points(x_best_distance, y + 1, x, y)

    def update_matrix(self):
        # We check if every point can be updated
        for y in reversed(range(len(self.matrix_content))):
            self.update_line(y)
