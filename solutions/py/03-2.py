import math

def intersection(l1, l2):
    return [value for value in l2 if value in l1]

def man_dist(point):
    return abs(point[0]) + abs(point[1])

wire1 = {}
wire2 = {}
# wire {(x,y) : dist}
for wire in (wire1, wire2):
    x = 0
    y = 0
    dx = 0
    dy = 0
    steps = 0
    for move in input().split(","):
        if move[0] == "D":
            dx = 0
            dy = -1
        elif move[0] == "U":
            dx = 0
            dy = 1
        elif move[0] == "R":
            dx = 1
            dy = 0
        elif move[0] == "L":
            dx = -1
            dy = 0
        for i in range(int(move[1:])):
            x += dx
            y += dy
            steps += 1
            wire[(x, y)] = steps

points = intersection(list(wire1.keys()), list(wire2.keys()))
length = wire1[points[0]] + wire2[points[0]]
for point in points[1:]:
    length = min(length, wire1[point] + wire2[point])
print(length)
