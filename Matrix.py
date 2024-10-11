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

# @todo -move the points (not only print the movement)
# @todo -use recurrence to move the points (i the point above me can move, then ill move too) (def check_if_i_can_move)
    def update_point(self, x, y):
        print(x, y)
        if y >= len(self.matrix_content)-1:
            print("down already")
        elif self.matrix_content[y + 1][x - 1] != 1:
            print("mid")
        elif self.matrix_content[y + 1][x - 2] != 1 and self.matrix_content[y + 1][x] != 1:
            print("both")
        elif x > 0 and self.matrix_content[y + 1][x - 2] != 1:
            print("left")
        elif x < len(self.matrix_content[y + 1])-1 and self.matrix_content[y + 1][x] != 1:
            print("right")
        else:
            print("can't move")
#
    def update_matrix(self):
        # We check if every point can be updated
        for y in range(len(self.matrix_content)).__reversed__():
            for x in range(len(self.matrix_content[y - 1])).__reversed__():
                # If the point is considered filled with something, we update its position
                match self.matrix_content[y - 1][x - 1]:
                    case 1:
                        self.update_point(x, y)
