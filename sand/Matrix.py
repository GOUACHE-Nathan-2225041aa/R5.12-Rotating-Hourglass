import math
import random


class Matrix:
    def __init__(self, matrix_content=[[0], [0]], wall=2, content=1, blank=0):
        self.matrix_content = matrix_content
        self.content = content
        self.blank = blank
        self.wall = wall

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

# @todo : finis ça bg j'ai trop la flemme
    def generate_hourglass(self, size, chance_of_content=0.2):
        matrix = []
        for i in range(size):
            matrix.append([])
            for j in range(size/2):

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
            # If the current x i the row is a particle and there is room under it, 
            # begin the calculus for the nearest blank space
            if (self.matrix_content[y][x] == self.content and y != len(self.matrix_content) - 1
                    and (self.blank in self.matrix_content[y + 1])):
                # Init the best distance and the x associated to it
                best_distance = float("inf")
                x_best_distance = -1
                # Going through the row under to check for blank spaces
                for lower_x in range(len(self.matrix_content[y + 1])):
                    if self.matrix_content[y + 1][lower_x] == self.blank:
                        # Calculate the distance between the 2 points then compares it to the best distance saved (Math)
                        distance_between_2_points = math.sqrt(abs(((x - lower_x) ** 2) + 1))
                        if distance_between_2_points < best_distance:
                            best_distance = distance_between_2_points
                            x_best_distance = lower_x
                # @todo : normalize the water level
                # If we found a place to move the point to...
                if x_best_distance != -1:
                    # Move to the left
                    if x_best_distance < x and self.matrix_content[y][x - 1] in [self.blank, self.content]:
                        self.switch_points(x - 1, y, x, y)
                        has_updated = True
                    # Move to the right
                    elif x_best_distance > x and self.matrix_content[y][x + 1] in [self.blank, self.content]:
                        self.switch_points(x + 1, y, x, y)
                        has_updated = True
                    # Insert in the blank space under
                    elif self.matrix_content[y + 1][x] == self.blank or (self.wall not in self.matrix_content[y + 1]):
                        self.switch_points(x_best_distance, y + 1, x, y)
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
