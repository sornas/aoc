import aoc20
import sys
from collections import defaultdict


def draw(hset, hdict):
    sqset = set()
    sqdict = dict()
    min_x = min_y = -10
    max_x = max_y =  10

    for hx, hy in hset:
        x = 2*hx + hy
        y = hy
        sqset.add((x, y))
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    for hx, hy in hdict:
        x = 2*hx + hy
        y = hy
        sqdict[(x, y)] = hdict[(hx, hy)]
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    s = "{} {} {} {}\n".format(min_x, max_x, min_y, max_y)
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in sqset:
                s += "*"
            else:
                s += " "

            if (x, y) in sqdict:
                s += str(sqdict[(x, y)])
            else:
                s += " "

            if (x, y) in sqset:
                s += "*"
            else:
                s += " "
        s += "\n"
    return s


def pt1(_in):
    # two coordinates
    # (
    #   x: W-E
    #   y: SW-NE
    # )
    tiles = set()

    for line in _in:
        x = y = 0
        i = 0
        while i < len(line):
            c = line[i]
            i += 1
            if c in "ns":
                c += line[i]
                i += 1

            if c == "e":
                x += 1
            elif c == "se":
                x += 1
                y -= 1
            elif c == "sw":
                y -= 1
            elif c == "w":
                x -= 1
            elif c == "nw":
                x -= 1
                y += 1
            elif c == "ne":
                y += 1

        p = (x, y)
        if p in tiles:
            tiles.remove(p)
        else:
            tiles.add(p)
    return(len(tiles))


def neighbours(p):
    #         y=+1
    #       E F
    # x=-1 D X A x=+1
    #       C B
    #    y=-1
    x, y = p
    return [
        (x+1, y),
        (x+1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x,   y+1),
        (x,   y-1),
    ]


def pt2(_in):
    # two coordinates
    # (
    #   x: W-E
    #   y: SW-NE
    # )
    active = set()

    for line in _in:
        x = y = 0
        i = 0
        while i < len(line):
            c = line[i]
            i += 1
            if c in "ns":
                c += line[i]
                i += 1

            if c == "e":
                x += 1
            elif c == "se":
                x += 1
                y -= 1
            elif c == "sw":
                y -= 1
            elif c == "w":
                x -= 1
            elif c == "nw":
                x -= 1
                y += 1
            elif c == "ne":
                y += 1

        p = (x, y)
        if p in active:
            active.remove(p)
        else:
            active.add(p)

    board = defaultdict(lambda: 0)
    for p in active:
        for n in neighbours(p):
            board[n] += 1

    for i in range(100):
        new_board = defaultdict(lambda: 0)
        new_active = set()
        for p, deg in board.items():
            if p in active and not (deg == 0 or deg > 2):
                new_active.add(p)
                for n in neighbours(p):
                    new_board[n] += 1
            elif p not in active and deg == 2:
                new_active.add(p)
                for n in neighbours(p):
                    new_board[n] += 1

        board = new_board
        active = new_active
    return len(active)


if __name__ == "__main__":
    _in = aoc20.read_input(sys.argv[1:], 24)
    print(pt1(_in))
    print(pt2(_in))
