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
    

def main():
    sensors = set()
    beacons = set()
    not_beacons = set()
    target_y = 2000000
    for line in sys.stdin.readlines():
        match = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        sx, sy, cx, cy = list(map(int, match.groups()))
        sensors |= {(sx, sy)}
        beacons |= {(cx, cy)}

        cd = md((sx, sy), (cx, cy))
        for dy in range(cd+1):
            if sy + dy == target_y:
                for dx in range((cd - dy) + 1):
                    not_beacons |= {(sx + dx, sy + dy)}
                    not_beacons |= {(sx - dx, sy + dy)}
            if sy - dy == target_y:
                for dx in range((cd - dy) + 1):
                    not_beacons |= {(sx + dx, sy - dy)}
                    not_beacons |= {(sx - dx, sy - dy)}

        td = abs(sy - target_y)
        if td > target_y:
            continue
        # which of them are on this line?
        # symmetrical triangle
        # cd - td: max distance - distance to target y => how many on target line
        on_target = abs(cd - td)
        for x in range(-on_target, on_target + 1):
            pass
            #not_beacons |= {(sx + x, target_y)}
    # vis(sensors, beacons, not_beacons)
    print(len(not_beacons - beacons))

main()
