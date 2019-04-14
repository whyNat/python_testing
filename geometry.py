from geom2d import *


# l1 = (Point(3, 1), Point(0, 0), Point(1, 2))

# def x(p):
#     return p.x
#
# def y(p):
#     return p.y

#l2 = sorted(l1, key=p)

# Powyzsze funkcje mozna zastapic lambda:
# l2 = sorted(l1, key=lambda p: p.x)   # sortowanie wg osi x

# l2 = sorted(l1, key=lambda p: p.distance(Point(0,0)))   # sortowanie wg punktu (0,0) z wykorzystaniem funkcji distance
# print(l1)
# print(l2)

# list comprehension:
#l = [Point(i, i*i) for i in range(-5, 6)]

# obiekt map przekształcony na listę, który działa jak pętla for, dziala dla kazdego elementu listy
l = list(map(lambda i: Point(i, i*i), range(-5, 6)))

#l2 = [Point(el.x, -el.y) for el in l ]

l2 = list(map(lambda p: Point(p.x, -p.y), l))

# filtr listy:
l2 = list(filter(lambda p: p.x % 2 == 0, l))

print(l)
print(l2)