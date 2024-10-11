import random


class Matrix:
    def __init__(self, matrix_content=[]):
        self.matrix_content = matrix_content

    def __str__(self):
        printable_matrix = ""
        for i in range(len(self.matrix_content)):
            for j in range(len(self.matrix_content[i - 1])):
                printable_matrix += " " + str(self.matrix_content[i - 1][j - 1]) + " "
            printable_matrix += "\n"
        return printable_matrix

    def move_point(self, x, y, where):
        if where == "down":
            temp = self.matrix_content[y][x - 1]
            self.matrix_content[y][x - 1] = self.matrix_content[y - 1][x - 1]
            self.matrix_content[y - 1][x - 1] = temp
        elif where == "down-left":
            temp = self.matrix_content[y][x - 2]
            self.matrix_content[y][x - 2] = self.matrix_content[y - 1][x - 1]
            self.matrix_content[y - 1][x - 1] = temp
        elif where == "down-right":
            temp = self.matrix_content[y][x]
            self.matrix_content[y][x] = self.matrix_content[y - 1][x - 1]
            self.matrix_content[y - 1][x - 1] = temp

    # @todo -delete the temp values
    # @todo -make the final result completely flat
    def update_point(self, x, y):
        if self.matrix_content[y][x - 1] != 0:
            # The point drops by 1
            self.move_point(x, y, "down")
        elif self.matrix_content[y][x - 2] != 0 and self.matrix_content[y][x] != 0:
            if bool(random.getrandbits(1)):
                self.move_point(x, y, "down-right")
            else:
                self.move_point(x, y, "down-left")
        elif x > 0 and self.matrix_content[y][x - 2] != 0:
            # The point drops by 1 on the left
            self.move_point(x, y, "down-left")
            return True
        elif x < len(self.matrix_content[y - 1]) - 1 and self.matrix_content[y][x] != 0:
            # The point drops by 1 on the right
            self.move_point(x, y, "down-right")

    def update_matrix(self):
        # We check if every point can be updated
        for y in range(len(self.matrix_content)).__reversed__():
            for x in range(len(self.matrix_content[y - 1])).__reversed__():
                # If the point is considered filled with something, we update its position
                if self.matrix_content[y - 1][x - 1] == 0 and not (y >= len(self.matrix_content) - 1):
                    self.update_point(x, y)
