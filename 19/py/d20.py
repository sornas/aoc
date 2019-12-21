import heapq as heap
import sys

def draw(maze, start=None, end=None, portals={}, min_x=0, max_x=0, min_y=0, max_y=0, around=None, visited=set()):
    maze = maze.copy()
    if start is not None:
        maze[start] = "S"
    if end is not None:
        maze[end] = "E"

    if around is not None:
        min_x = around[0]-5
        max_x = around[0]+5
        min_y = around[1]-5
        max_y = around[1]+5
    if around is None and max_x == 0:
        for p in maze:
            max_x = max(p[0], max_x)
    if around is None and max_y == 0:
        for p in maze:
            max_y = max(p[1], max_y)
    s = ""
    for y in range(min_y, max_y+1):
        s += "\n"
        for x in range(min_x, max_x+1):
            p = (x,y)
            if around is not None and p == around:
                s += "X"
            if p in portals:
                s += "O"
            elif p in visited:
                s += "x"
            elif p in maze:
                s += maze[p]
            else:
                s += " "
    return s

def neighbours(p):
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), \
            (p[0], p[1]+1), (p[0], p[1]-1)]

def pt1(input):
    maze = {}
    walls = set()
    tiles = set()
    max_x = 0
    max_y = 0

    for y in range(len(input)):
        max_y = max(max_y, y)
        for x in range(len(input[y])):
            max_x = max(max_x, x)
            p = (x,y)
            c = input[y][x]
            maze[p] = c
            if c == "#":
                walls.add(p)
            elif c == ".":
                tiles.add(p)
            else:
                del maze[p]

    alone_portals = {}  # { "JZ" : (25,50) ... }
    portal_pairs = {}  # { (25,50) : (30,30) ... ] contains reverse as well
    portals = set()
    found_portals = set()
    checked = set()
    for y in range(len(input)):
        for x in range(len(input[y])):
            p = (x,y)
            if p in checked:
                continue
            c = input[y][x]
            if c.isalpha():
                # find the other letter
                p2 = None
                if x < max_x and input[y][x+1].isalpha():
                    portal = "".join([c, input[y][x+1]])
                    p2 = (x+1, y)
                elif x > 0 and input[y][x-1].isalpha():
                    portal = "".join([input[y][x-1], c])
                    p2 = (x-1, y)
                elif y < max_y and input[y+1][x].isalpha():
                    portal = "".join([c, input[y+1][x]])
                    p2 = (x, y+1)
                elif y > 0 and input[y-1][x].isalpha():
                    portal = "".join([input[y-1][x], c])
                    p2 = (x, y-1)
                if p2 is None:
                    print("bad label near", p)
                    sys.exit()
                checked.add(p2)
                # find the empty space
                location = None
                for n in neighbours(p) + neighbours(p2):
                    if n in tiles:
                        location = n
                if location is None:
                    print("invalid location near", p)
                    print(draw(maze, around=p))
                if portal == "AA":
                    start = location
                    continue
                if portal == "ZZ":
                    end = location
                    continue
                if portal in alone_portals:
                    portal_pairs[alone_portals[portal]] = location
                    portal_pairs[location] = alone_portals[portal]
                    del alone_portals[portal]
                    continue
                if portal in found_portals:
                    print("found double portal near", p)
                    print(draw(maze, around=p))
                    sys.exit()
                alone_portals[portal] = location
    #print(draw(maze, start=start, end=end, portals=portal_pairs))

    INSIDE_X_LO = 20
    INSIDE_X_HI = 120
    INSIDE_Y_LO = 20
    INSIDE_Y_HI = 100

    # find shortest path between each portal (and start/end)
    h = []
    visited = set(start)
    heap.heappush(h, (0, start))
    while len(h) > 0:
        cur = heap.heappop(h)
        dist = cur[0]
        point = cur[1]
        x = point[0]
        y = point[1]
        if point == end:
            return dist
        if point in portal_pairs:
            dist += 1
            point = portal_pairs[point]
        for n in neighbours(point):
            if n not in maze:
                continue
            if n in visited:
                continue
            if n not in walls:
                visited.add(n)
                heap.heappush(h, (dist+1, n))

def pt2(input):
    maze = {}
    walls = set()
    tiles = set()
    max_x = 0
    max_y = 0

    for y in range(len(input)):
        max_y = max(max_y, y)
        for x in range(len(input[y])):
            max_x = max(max_x, x)
            p = (x,y)
            c = input[y][x]
            maze[p] = c
            if c == "#":
                walls.add(p)
            elif c == ".":
                tiles.add(p)
            else:
                del maze[p]

    alone_portals = {}  # { "JZ" : (25,50) ... }
    portal_pairs = {}  # { (25,50) : (30,30) ... ] contains reverse as well
    portals = set()
    found_portals = set()
    checked = set()
    for y in range(len(input)):
        for x in range(len(input[y])):
            p = (x,y)
            if p in checked:
                continue
            c = input[y][x]
            if c.isalpha():
                # find the other letter
                p2 = None
                if x < max_x and input[y][x+1].isalpha():
                    portal = "".join([c, input[y][x+1]])
                    p2 = (x+1, y)
                elif x > 0 and input[y][x-1].isalpha():
                    portal = "".join([input[y][x-1], c])
                    p2 = (x-1, y)
                elif y < max_y and input[y+1][x].isalpha():
                    portal = "".join([c, input[y+1][x]])
                    p2 = (x, y+1)
                elif y > 0 and input[y-1][x].isalpha():
                    portal = "".join([input[y-1][x], c])
                    p2 = (x, y-1)
                if p2 is None:
                    print("bad label near", p)
                    sys.exit()
                checked.add(p2)
                # find the empty space
                location = None
                for n in neighbours(p) + neighbours(p2):
                    if n in tiles:
                        location = n
                if location is None:
                    print("invalid location near", p)
                    print(draw(maze, around=p))
                if portal == "AA":
                    start = location
                    continue
                if portal == "ZZ":
                    end = location
                    continue
                if portal in alone_portals:
                    portal_pairs[alone_portals[portal]] = location
                    portal_pairs[location] = alone_portals[portal]
                    del alone_portals[portal]
                    continue
                if portal in found_portals:
                    print("found double portal near", p)
                    print(draw(maze, around=p))
                    sys.exit()
                alone_portals[portal] = location
    #print(draw(maze, start=start, end=end, portals=portal_pairs))

    INSIDE_X_LO = 20
    INSIDE_X_HI = 120
    INSIDE_Y_LO = 20
    INSIDE_Y_HI = 100

    # find shortest path between each portal (and start/end)
    h = []
    visited = {0: set()}
    visited[0].add(start)
    heap.heappush(h, (0, 0, start))
    while len(h) > 0:
        cur = heap.heappop(h)
        dist = cur[0]
        dimen = cur[1]
        point = cur[2]
        x = point[0]
        y = point[1]
        if point == end and dimen == 0:
            return dist
        if point in portal_pairs:
            if INSIDE_X_LO < x < INSIDE_X_HI and INSIDE_Y_LO < y < INSIDE_Y_HI:
                # inside donut
                dimen += 1
            else:
                if dimen == 0:
                    continue
                dimen -= 1
            dist += 1
            if dimen not in visited:
                visited[dimen] = set()
            point = portal_pairs[point]
        for n in neighbours(point):
            if n not in maze:
                continue
            if n in visited[dimen]:
                continue
            if n not in walls:
                visited[dimen].add(n)
                heap.heappush(h, (dist+1, dimen, n))

if __name__ == "__main__":
    input = open("../input/20", "r").readlines()
    print(pt1(input))
    print(pt2(input))

