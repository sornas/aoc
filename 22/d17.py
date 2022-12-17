import copy
import sys

def parse_shape(s):
    res = []
    for y, l in enumerate(reversed(s.strip().split("\n"))):
        for x, c in enumerate(l):
            if c == "#":
                res.append([x, y])
    return res

def visualize(cur, rock):
    max_y = max(y for _, y in cur)
    max_y2 = max(y for _, y in rock)
    max_y = max(max_y, max_y2)
    cur = list(map(tuple, cur))

    for y in list(range(max_y+2))[::-1]:
        for x in range(7):
            p = (x, y)
            if p in cur:
                print("@", end="")
            elif p in rock:
                print("#", end="")
            else:
                print(".", end="")
        print()



def main():
    pat = open(sys.argv[1]).read().strip()
    shapes = [
        """
####
        """,

        """
.#.
###
.#.
        """,

        """
..#
..#
###
        """,

        """
#
#
#
#
        """,

        """
##
##
        """,
    ]

    rock = {(x, 0) for x in range(7)}

    shapes = list(map(parse_shape, shapes))
    shape_idx = 0
    cur = copy.deepcopy(shapes[shape_idx])
    shape_idx += 1

    def move_x(n):
        for pos in cur:
            pos[0] += n

    def move_y(n):
        for pos in cur:
            pos[1] += n

    def collision():
        return any(tuple(p) in rock for p in cur) or any(x < 0 for x, _ in cur) or any(x >= 7 for x, _ in cur)

    # starts two to the right
    move_x(2)

    # and three above the highest y
    highest = max(y for _, y in rock)
    move_y(highest + 4)


    stopped = 0
    steps = 0
    while stopped < 2022:
        # blow
        if pat[steps] == ">":
            move_x(1)
            if collision():
                move_x(-1)
        else:
            move_x(-1)
            if collision():
                move_x(1)
        steps = (steps + 1) % len(pat)
        # try move down
        move_y(-1)
        if collision():
            move_y(1)
            rock |= set(map(tuple, cur))
            cur = copy.deepcopy(shapes[shape_idx])
            shape_idx = (shape_idx + 1) % len(shapes)
            stopped += 1
            move_x(2)
            highest = max(y for _, y in rock)
            move_y(highest + 4)
        print(stopped, max(y for _, y in rock))
    print(stopped, max(y for _, y in rock))


main()
