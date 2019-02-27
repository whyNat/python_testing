from math import sqrt
# import pierwiastka kwadratowego

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # obliczenie odległości pomiędzy punktami
    def distance(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        return sqrt(dx*dx + dy * dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y