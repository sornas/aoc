import re
import sys

def md(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    return abs(p1x-p2x) + abs(p1y-p2y)

def vis(sensors, beacons, not_beacons):
    lo_x = min(x for x, _ in sensors | beacons | not_beacons)
    lo_y = min(y for _, y in sensors | beacons | not_beacons)
    hi_x = max(x for x, _ in sensors | beacons | not_beacons)
    hi_y = max(y for _, y in sensors | beacons | not_beacons)

    for y in range(lo_y-2, hi_y+3):
        for x in range(lo_x-2, hi_x+3):
            p = (x, y)
            if p in sensors:
                print("S", end="")
            elif p in beacons:
                print("B", end="")
            elif p in not_beacons:
                print("#", end="")
            else:
                print(".", end="")
        print()
    
# IDEA
# the point we look for will be 1 step out of the border of one of the areas
# for each sensor, we now the distance to its beacon
# exactly 1 of the points will be farther than that from all sensors

def main():
    sensors = dict()
    beacons = set()
    not_beacons = set()
    for line in sys.stdin.readlines():
        match = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        sx, sy, bx, by = list(map(int, match.groups()))
        s = (sx, sy)
        b = (bx, by)
        sb_distance = md(s, b)

        # for each sensor, what is the distance to its closest beacon
        sensors[s] = sb_distance
        beacons |= {b}

    # .........
    # ....c....
    # ...c#c...
    # ..c###c..
    # .cb#s##c.
    # ..c###c..
    # ...c#c...
    # ....c....
    # .........

    def try_cand(c):
        cx, cy = c
        return 0 <= cx <= 4000000 and 0 <= cy <= 4000000 and all(md(c, s) > dist for s, dist in sensors.items())

    candidates = set()
    for s, dist in sensors.items():
        print(s)
        sx, sy = s
        for dy in range(-dist-1, dist+2):
            if dy >= 0:
                dx = dist+1 - dy
            else:
                dx = dist+1 + dy
            candidate = (sx+dx, sy+dy)
            if try_cand(candidate):
                print(candidate, candidate[0] * 4000000 + candidate[1])
                return
            candidate = (sx-dx, sy+dy)
            if try_cand(candidate):
                print(candidate, candidate[0] * 4000000 + candidate[1])
                return
        # vis(set(sensors.keys()), beacons, candidates)
        # print()

main()
