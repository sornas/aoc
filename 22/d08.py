import sys
import math

def main():
    trees = {}
    lines = sys.stdin.readlines()
    h = len(lines)
    for y, line in enumerate(lines):
        w = len(line.strip())
        for x, c in enumerate(line.strip()):
            trees[(int(x), int(y))] = int(c)

    def in_range(x, y):
        return 0 <= x < w and 0 <= y < h

    visible = 0
    for y in range(h):
        for x in range(w):
            this_visible = False
            for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                this_visible_dir = True
                i = 1
                while in_range(x + d[0]*i, y + d[1]*i):
                    if trees[(x + d[0]*i, y + d[1]*i)] >= trees[(x, y)]:
                        this_visible_dir = False
                    i += 1
                this_visible |= this_visible_dir
            if this_visible:
                visible += 1
    print(visible)

    highest_scenic = 0
    for y in range(h):
        for x in range(w):
            in_dir = []
            for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                # down, right, left, up
                i = 1
                while in_range(x + d[0]*i, y + d[1]*i):
                    if trees[(x + d[0]*i, y + d[1]*i)] >= trees[(x, y)]:
                        i += 1
                        break
                    i += 1
                in_dir.append(i-1)
            scenic = math.prod(in_dir)
            print(x, y, in_dir, scenic)
            highest_scenic = max(scenic, highest_scenic)
    print(highest_scenic)



main()
