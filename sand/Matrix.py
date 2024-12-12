import math
import random


class Matrix:
    def __init__(self, matrix_content=[[0], [0]], wall=2, content=1, blank=0):
        self.matrix_content = matrix_content
        self.content = content
        self.blank = blank
        self.wall = wall
        self.movable = [content, blank]

    def generate_matrix(self, size, chance_of_content=0.2):
        matrix = []
        # Appends random contents to the matrix
        for i in range(size):
            matrix.append([])
            for j in range(size):
                if random.random() < chance_of_content:
                    matrix[i].append(self.content)
                else:
                    matrix[i].append(self.blank)
        self.matrix_content = matrix
        return matrix

    def generate_hourglass(self, size, chance_of_content=0.2):
        matrix = []
        # Building hourglass
        for line in range(size):
            # Left side
            matrix.append([])
            for Lcolumn in range(line):
                matrix[line].append(self.blank)
            matrix[line].append(self.wall)
            for Rcolumn in range(size - line - 1):
                if line == 0:
                    matrix[line].append(self.wall)
                elif random.random() < chance_of_content:
                    matrix[line].append(self.content)
                else:
                    matrix[line].append(self.blank)

            # Right side
            for Lcolumn in range(size - line - 1):
                if line == 0:
                    matrix[line].append(self.wall)
                elif random.random() < chance_of_content:
                    matrix[line].append(self.content)
                else:
                    matrix[line].append(self.blank)
            matrix[line].append(self.wall)
            for Rcolumn in range(line):
                matrix[line].append(self.blank)

        # Remove last line where the content can't pass
        matrix.pop()

        margin = [0] * len(matrix[0])

        matrix.insert(0, margin)

        matrix.extend(reversed([row.copy() for row in matrix]))

        self.matrix_content = matrix
        return matrix

    # A user-friendly way to display the matrix's content
    def __str__(self):
        printable_matrix = ""
        for i in range(len(self.matrix_content)):
            for j in range(len(self.matrix_content[i])):
                printable_matrix += " " + str(self.matrix_content[i][j]) + " "
            printable_matrix += "\n"
        return printable_matrix

    # Switch 2 points' position
    def switch_points(self, x1, y1, x2, y2):
        temp = self.matrix_content[y1][x1]
        self.matrix_content[y1][x1] = self.matrix_content[y2][x2]
        self.matrix_content[y2][x2] = temp

    def update_line(self, y):
        # Init of the update check
        has_updated = False
        # Go through the y row
        for x in range(len(self.matrix_content[y])):
            if x % 2 == 0:
                index = x // 2
            else:
                index = len(self.matrix_content[y]) - (x // 2) - 1

            # If the current index in the row is a particle and there is room under it,
            # begin the calculus for the nearest blank space
            if (self.matrix_content[y][index] == self.content and y != len(self.matrix_content) - 1
                    and (self.blank in self.matrix_content[y + 1])):
                # Under
                if self.matrix_content[y + 1][index] == self.blank:
                    self.switch_points(index, y, index, y + 1)
                    has_updated = True
                # Under left
                elif ((self.matrix_content[y + 1][index - 1] == self.blank) and
                      (any(check in self.movable for check in
                           [self.matrix_content[y + 1][index], self.matrix_content[y][index - 1]]))):
                    self.switch_points(index, y, index - 1, y + 1)
                    has_updated = True
                # Under right
                elif ((self.matrix_content[y + 1][index + 1] == self.blank) and
                      (any(check in self.movable for check in
                           [self.matrix_content[y + 1][index], self.matrix_content[y][index + 1]]))):
                    self.switch_points(index, y, index + 1, y + 1)
                    has_updated = True

        return has_updated

    def update_matrix(self):
        has_updated = False
        # We check if every point can be updated
        for y in reversed(range(len(self.matrix_content))):
            if self.update_line(y):
                has_updated = True
        # Return if one or more points has been updated
        return not has_updated

    # Function to rotate a matrix (-90°)
    def rotate_matrix(self):
        self.matrix_content = [list(reversed(col)) for col in zip(*self.matrix_content)]
        return self.matrix_content
