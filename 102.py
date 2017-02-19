class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


    def dot(self, other):
        return self.x * other.x + self.y * other.y


def solve(line):
    points = list(map(int,line.split(',')))
    A = Vector(points[0], points[1])
    B = Vector(points[2], points[3])
    C = Vector(points[4], points[5])
    O = Vector(0, 0)

    v0 = C - A
    v1 = B - A
    v2 = O - A

    d00 = v0.dot(v0)
    d01 = v0.dot(v1)
    d02 = v0.dot(v2)
    d11 = v1.dot(v1)
    d12 = v1.dot(v2)

    m = 1/(d00 * d11 - d01 * d01)

    u = (d11 * d02 - d01 * d12) * m
    v = (d00 * d12 - d01 * d02) * m

    return u >= 0 and v >= 0 and u + v < 1

with open("p102_triangles.txt") as f:
    count = 0
    for line in f:
        res = solve(line.strip())
        if res:
            count += 1

    print(count)
