from profilehooks import coverage
import math

def intersection(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    return [value for value in l2 if value in l1]

def man_dist(point):
    return abs(point[0]) + abs(point[1])

#@coverage
def pt1(input):
    wire1 = []
    wire2 = []
    for wire, moves in zip((wire1, wire2), (input[0], input[1])):
        x = 0
        y = 0
        dx = 0
        dy = 0
        for move in moves.split(","):
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
                wire.append((x, y))
    points = intersection(wire1, wire2)
    dist = man_dist(points[0])
    for point in points[1:]:
        dist = min(dist, man_dist(point))
    return dist

#@coverage
def pt2(input):
    wire1 = {}
    wire2 = {}
    # wire {(x,y) : dist}
    for wire, moves in zip((wire1, wire2), (input[0], input[1])):
        x = 0
        y = 0
        dx = 0
        dy = 0
        steps = 0
        for move in moves.split(","):
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
    return length

if __name__ == "__main__":
    input = open("../input/03", "r").readlines()
    print(pt1(input))
    print(pt2(input))
