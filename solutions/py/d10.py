import math
import os
import queue
import sys
import time

def red(dcoord):
    dx = dcoord[0]
    dy = dcoord[1]
    if dx == 0:
        return (0, (1 if dy > 0 else -1))
    if dy == 0:
        return ((1 if dx > 0 else -1), 0)
    gcd = math.gcd(dx, dy)
    return (dx // gcd, dy // gcd)

def angle(x, y):  # from y-axis, clockwise
    if x >= 0 and y > 0:
        return math.atan(abs(x/y))
    if x > 0 and y <= 0:
        return math.atan(abs(y/x)) + math.pi/2
    if x <= 0 and y < 0:
        return math.atan(abs(x/y)) + math.pi
    else:
        return math.atan(abs(y/x)) + 3*math.pi / 2

def pt1(input):
    asteroids = set()
    res = {}

    max_x = len(input[0].rstrip())
    max_y = len(input)

    for y in range(max_y):
        for x in range(max_x):
            if input[y][x] == "#":
                asteroids.add((x,y))

    for a in asteroids:
        candidates = set(asteroids.copy())
        candidates.remove(a)
        seen = set()
        while len(candidates) > 0:
            c = candidates.pop()
            seen.add(c)
            dx = c[0] - a[0]
            dy = c[1] - a[1]
            x = a[0]
            y = a[1]
            x += dx
            y += dy
            dx, dy = red((dx, dy))
            x += dx
            y += dy
            while x < max_x and y < max_y and x >= 0 and y >= 0:
                if (x, y) in candidates:
                    candidates.remove((x, y))
                if (x, y) in seen:
                    seen.remove((x, y))
                x += dx
                y += dy
        res[a] = seen

    best = [0, 0, 0]
    for coord in res:
        amount = len(res[coord])
        if amount > best[0]:
            best = [amount, coord, res[coord]]
    return (best[1], best[0])

def pt2(input):
    asteroids = set()
    res = {}

    max_x = len(input[0].rstrip())
    max_y = len(input)

    for y in range(max_y):
        for x in range(max_x):
            if input[y][x] == "#":
                asteroids.add((x,y))

    for a in asteroids:
        candidates = set(asteroids.copy())
        candidates.remove(a)
        seen = set()
        while len(candidates) > 0:
            c = candidates.pop()
            seen.add(c)
            dx = c[0] - a[0]
            dy = c[1] - a[1]
            x = a[0]
            y = a[1]
            x += dx
            y += dy
            dx, dy = red((dx, dy))
            x += dx
            y += dy
            while x < max_x and y < max_y and x >= 0 and y >= 0:
                if (x, y) in candidates:
                    candidates.remove((x, y))
                if (x, y) in seen:
                    seen.remove((x, y))
                x += dx
                y += dy
        res[a] = seen

    best = [0, 0, 0]
    for coord in res:
        amount = len(res[coord])
        if amount > best[0]:
            best = [amount, coord, res[coord]]
    asteroids.remove(best[1])
    x0 = best[1][0]
    y0 = best[1][1]

    angles = {}
    q = queue.Queue()
    for a in asteroids:
        angles[a] = angle(a[0] - x0, y0 - a[1])

    for k, v in sorted(angles.items(), key=lambda item: item[1]):
        if k in best[2]:
            q.put(k)

    destroyed = 1
    while not q.empty():
        asteroid = q.get()
        if destroyed == 200:
            return (asteroid, asteroid[0]*100 + asteroid[1])
        asteroids.remove(asteroid)
        destroyed += 1

        # add next asteroid behind to queue
        dx = asteroid[0] - x0
        dy = asteroid[1] - y0
        x = x0
        y = y0
        x += dx
        y += dy
        dx, dy = red((dx, dy))
        x += dx
        y += dy
        while x < max_x and y < max_y and x >= 0 and y >= 0:
            if (x, y) in asteroids:
                q.put((x, y))
                break
            x += dx
            y += dy

def print_map(coords, w, h):
    time.sleep(0.01)
    os.system("clear")
    s = ""
    for y in range(w):
        for x in range(h):
            s += (coords[(x, y)] + " ") if (x,y) in coords else "  "
        s += "\n"
    print(s)

def visualize(input):
    asteroids = set()
    res = {}

    max_x = len(input[0].rstrip())
    max_y = len(input)

    for y in range(max_y):
        for x in range(max_x):
            if input[y][x] == "#":
                asteroids.add((x,y))

    #print_map(asteroids, max_x, max_y)

    for a in asteroids:
        print(a)
        time.sleep(3)
        candidates = set(asteroids.copy())
        candidates.remove(a)
        seen = set()
        while len(candidates) > 0:
            #print(len(candidates))
            time.sleep(0.02)
            union = {a: "\u2588"}
            for c in candidates:
                union[c] = "C"
            for s in seen:
                union[s] = "s"
            print_map(union, max_x, max_y)
            c = candidates.pop()
            seen.add(c)
            dx = c[0] - a[0]
            dy = c[1] - a[1]
            x = a[0]
            y = a[1]
            x += dx
            y += dy
            dx, dy = red((dx, dy))
            x += dx
            y += dy
            while x < max_x and y < max_y and x >= 0 and y >= 0:
                if (x, y) in candidates:
                    candidates.remove((x, y))
                if (x, y) in seen:
                    seen.remove((x, y))
                x += dx
                y += dy
        res[a] = seen

    best = [0, 0, 0]
    for coord in res:
        amount = len(res[coord])
        if amount > best[0]:
            best = [amount, coord, res[coord]]
    asteroids.remove(best[1])
    x0 = best[1][0]
    y0 = best[1][1]

    angles = {}
    q = queue.Queue()
    for a in asteroids:
        angles[a] = angle(a[0] - x0, y0 - a[1])

    for k, v in sorted(angles.items(), key=lambda item: item[1]):
        if k in best[2]:
            q.put(k)

    destroyed = 1
    while not q.empty():
        #print_map(asteroids, max_x, max_y)
        asteroid = q.get()
        if destroyed == 200:
            return (asteroid, asteroid[0]*100 + asteroid[1])
        asteroids.remove(asteroid)
        destroyed += 1

        # add next asteroid behind to queue
        dx = asteroid[0] - x0
        dy = asteroid[1] - y0
        x = x0
        y = y0
        x += dx
        y += dy
        dx, dy = red((dx, dy))
        x += dx
        y += dy
        while x < max_x and y < max_y and x >= 0 and y >= 0:
            if (x, y) in asteroids:
                q.put((x, y))
                break
            x += dx
            y += dy
if __name__ == "__main__":
    import cProfile

    input = open("../input/10","r").readlines()
    visualize(input)
    #cProfile.run("pt1(input)")
    #cProfile.run("pt2(input)")
    print(pt1(input))
    print(pt2(input))
