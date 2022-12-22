import regex
import sys

def left(dx, dy):
    return (dy, -dx)

def right(dx, dy):
    return (-dy, dx)

def add(p1x, p1y, p2x, p2y):
    return (p1x + p2x, p1y + p2y)

def main():
    m, inst = sys.stdin.read().split("\n\n")
    walls = set()
    tiles = set()
    for y, line in enumerate(m.split("\n")):
        for x, c in enumerate(line):
            if c == ".":
                tiles.add((x, y))
            elif c == "#":
                walls.add((x, y))
    inside = walls | tiles
    pos = (min(x for x, y in tiles if y == 0), 0)
    direction = (1, 0)

    def wrap(px, py, d):
        if d == (1, 0):
            # right, wrap left
            return (min(x for x, y in inside if y == py), py)
        elif d == (-1, 0):
            # left, wrap right
            return (max(x for x, y in inside if y == py), py)
        elif d == (0, 1):
            # down, wrap up
            return (px, min(y for x, y in inside if x == px))
        elif d == (0, -1):
            # up, wrap down
            return (px, max(y for x, y in inside if x == px))
        else:
            print(":(")
            sys.exit()
            

    for inst in regex.match(r"((\d+)|[LR])*", inst).captures(1):
        print(inst)
        if inst == "L":
            direction = left(*direction)
            print(1, direction)
        elif inst == "R":
            direction = right(*direction)
            print(1, direction)
        else:
            for _ in range(int(inst)):
                new_pos = add(*pos, *direction)
                print(2, new_pos)
                # wrap around, if needed
                if new_pos not in inside:
                    new_pos = wrap(*new_pos, direction)
                    print(3, new_pos)
                # if wall, stop moving
                if new_pos in walls:
                    break
                pos = new_pos
    if direction == (1, 0):
        facing = 0
    elif direction == (0, 1):
        facing = 1
    elif direction == (-1, 0):
        facing = 2
    elif direction == (0, -1):
        facing = 3
    else:
        print(":(")
        sys.exit()
    print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + facing)

main()
