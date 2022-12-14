import itertools
import sys

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def main():
    walls = set()
    for line in sys.stdin.readlines():
        segs = line.split(" -> ")
        segs = [(int(seg.split(",")[0]), int(seg.split(",")[1])) for seg in segs]
        for i in range(len(segs) - 1):
            if segs[i][0] == segs[i + 1][0]:
                start = min(segs[i][1], segs[i + 1][1])
                end = max(segs[i][1], segs[i + 1][1])
                walls |= set(zip(itertools.repeat(segs[i][0]), range(start, end + 1)))
            else:
                start = min(segs[i][0], segs[i + 1][0])
                end = max(segs[i][0], segs[i + 1][0])
                walls |= set(zip(range(start, end + 1), itertools.repeat(segs[i][1])))
    max_y = max(y for _, y in walls)

    sand = set()
    cur = (500, 0)
    while True:
        # try to move down
        prev = cur
        down = add(cur, (0, 1))
        left = add(cur, (-1, 1))
        right = add(cur, (1, 1))
        for cand in [down, left, right]:
            if cand not in walls and cand not in sand:
                cur = cand
                break
        if cur == prev:
            # everything is blocked, come at rest
            sand |= {cur}
            cur = (500, 0)
            continue
        if cur[1] > max_y:
            # fell off + L + ratio
            print(len(sand))
            break

    sand = set()
    cur = (500, 0)
    while True:
        # try to move down
        prev = cur
        down = add(cur, (0, 1))
        left = add(cur, (-1, 1))
        right = add(cur, (1, 1))
        for cand in [down, left, right]:
            if cand not in walls and cand not in sand:
                cur = cand
                break
        if cur == prev or cur[1] == max_y + 1:
            if cur == (500, 0):
                print(len(sand) + 1)
                break
            # everything is blocked, come at rest
            sand |= {cur}
            cur = (500, 0)
            continue


main()
