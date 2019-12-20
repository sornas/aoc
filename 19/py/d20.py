import heapq as heap
import sys

input = open("../input/20", "r").readlines()

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

print(tiles)

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
            print(c, "at", p)
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
            print(portal, "found when checking", p2)
            checked.add(p2)
            # find the empty space
            location = None
            for n in neighbours(p) + neighbours(p2):
                if n in tiles:
                    print("found tile at", n)
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
print(draw(maze, start=start, end=end, portals=portal_pairs))

# find shortest path between each portal (and start/end)
h = []
visited = set()
visited.add(start)
heap.heappush(h, (0, start))
while len(h) > 0:
    #print(draw(maze, start=start, end=end, portals=portal_pairs, visited=visited))
    cur = heap.heappop(h)
    dist = cur[0]
    point = cur[1]
    if point == end:
        print(dist)
        break
    if point in portal_pairs:
        point = portal_pairs[point]
        dist += 1
    for n in neighbours(point):
        if n not in maze:
            continue
        if n in visited:
            continue
        if n not in walls:
            visited.add(n)
            heap.heappush(h, (dist+1, n))
