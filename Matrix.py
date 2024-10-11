import random

# @todo : fix bug last line afk

class Matrix:
    def __init__(self, matrix_content=[], content=0, space=" ", ):
        self.matrix_content = matrix_content
        self.content = content
        self.space = space

    def __str__(self):
        print(self.matrix_content)
        printable_matrix = ""
        for i in range(len(self.matrix_content)):
            for j in range(len(self.matrix_content[i])):
                printable_matrix += " " + str(self.matrix_content[i][j]) + " "
            printable_matrix += "\n"
        return printable_matrix

    # @todo -delete the temp values
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
        elif where == "down-somewhere":
            print("Je peux m'insérer là")

    # @todo -make the final result completely flat
    def update_point(self, x, y):
        if y >= len(self.matrix_content):
            pass
        elif self.matrix_content[y][x - 1] != self.content:
            # The point drops by 1
            self.move_point(x, y, "down")
        elif self.matrix_content[y][x - 2] != self.content and self.matrix_content[y][x] != self.content:
            if bool(random.getrandbits(1)):
                self.move_point(x, y, "down-right")
            else:
                self.move_point(x, y, "down-left")
        elif x > 0 and self.matrix_content[y][x - 2] != self.content:
            # The point drops by 1 on the left
            self.move_point(x, y, "down-left")
            return True
        elif x < len(self.matrix_content[y - 1]) - 1 and self.matrix_content[y][x] != self.content:
            # The point drops by 1 on the right
            self.move_point(x, y, "down-right")
        # @todo Implement here something to merge the point in the line under if the line under isn't full
        elif self.content not in self.matrix_content[y]:
            self.move_point(x, y, "down-somewhere")

    def update_matrix(self):
        print(self.matrix_content)
        # We check if every point can be updated
        for y in range(len(self.matrix_content)-1).__reversed__():
            for x in range(len(self.matrix_content[y - 1])).__reversed__():
                # If the point is considered filled with something, we update its position
                if self.matrix_content[y - 1][x - 1] == self.content:
                    self.update_point(x, y)
