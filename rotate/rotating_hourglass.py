import math
import matplotlib.pyplot as plt


def mult(A, v):
    result = [0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(v)):
            result[i] += A[i][j] * v[j]
    return result


def rotate(v, T):
    return mult([[math.cos(T), -math.sin(T)], [math.sin(T), math.cos(T)]], v)


class Quad:
    def __init__(self, coor_a, coor_b, coor_c, coor_d):
        self.coor_a = coor_a
        self.coor_b = coor_b
        self.coor_c = coor_c
        self.coor_d = coor_d

    def getMiddle(self):
        x = (self.coor_a[0] + self.coor_b[0] + self.coor_c[0]) / 3
        y = (self.coor_a[1] + self.coor_b[1] + self.coor_c[1]) / 3
        return [x, y]

    def rotate(self, T):
        self.coor_a = mult([[math.cos(T), -math.sin(T)], [math.sin(T), math.cos(T)]], self.coor_a)
        self.coor_b = mult([[math.cos(T), -math.sin(T)], [math.sin(T), math.cos(T)]], self.coor_b)
        self.coor_c = mult([[math.cos(T), -math.sin(T)], [math.sin(T), math.cos(T)]], self.coor_c)
        self.coor_d = mult([[math.cos(T), -math.sin(T)], [math.sin(T), math.cos(T)]], self.coor_d)

    def getCoor(self):
        return [self.coor_a, self.coor_b, self.coor_c, self.coor_d]


# Create the triangle object
q = Quad([-0.2, 0], [-3, -4], [3, -4], [0.2, 0])
q2 = Quad([0.2, 0], [3, 4], [-3, 4], [-0.2, 0])

# Initialize plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

# Set fixed axis limits
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')

# Animation loop
while True:
    plt.clf()  # Clear the figure
    ax = fig.add_subplot(111)

    # Set fixed axis limits again after clearing the plot
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')

    # Update triangle coordinates after rotation
    q.rotate(math.pi / 40)
    q2.rotate(math.pi / 40)

    # Prepare data for plotting

    x = [q.getCoor()[i][0] for i in range(4)]
    x += [q2.getCoor()[i][0] for i in range(4)]
    y = [q.getCoor()[i][1] for i in range(4)]
    y += [q2.getCoor()[i][1] for i in range(4)]


    # Plot the points and edges of the quad
    ax.plot(x, y)

    # Update the plot
    plt.draw()
    plt.pause(0.001)