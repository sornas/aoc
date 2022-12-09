import sys

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def move_towards(h, t):
    dx = dy = 0
    if abs(h[0] - t[0]) <= 1 and abs(h[1]-t[1]) <= 1:
        return t
    if h[0] > t[0]:
        dx = 1
    if h[0] < t[0]:
        dx = -1
    if h[1] > t[1]:
        dy = 1
    if h[1] < t[1]:
        dy = -1
    return add(t, (dx, dy))

def main():
    knots = [(0, 0) for _ in range(10)]
    seen1 = set()
    seen2 = set()
    for move in sys.stdin.readlines():
        d, l = move.strip().split(" ")
        l = int(l)
        print(d, l)
        if d == "R":
            dd = (1, 0)
        elif d == "L":
            dd = (-1, 0)
        elif d == "U":
            dd = (0, -1)
        elif d == "D":
            dd = (0, 1)
        for _ in range(l):
            knots[0] = add(knots[0], dd)
            for k in range(9):
                knots[k+1] = move_towards(knots[k], knots[k+1])
            seen1.add(knots[1])
            seen2.add(knots[-1])
    print(len(seen1))
    print(len(seen2))

main()
