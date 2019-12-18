import time
import collections
import heapq as heap
import sys

f = open("../input/18", "r").readlines()

def neighbours(p):
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), \
            (p[0], p[1]+1), (p[0], p[1]-1)]

def path(start: tuple, end:tuple, board:dict, keys={}, doors={}, draw_search=False):
    ''' Find the shortest path between two points '''
    if start == end:
        return collections.deque()
    visited = set()
    h = []
    heap.heappush(h, (0, start, collections.deque()))
    while True:
        if len(h) == 0:
            print(visited)
            return
        cur = heap.heappop(h)
        for n in neighbours(cur[1]):
            if n == end:
                cur[2].append(n)
                if draw_search:
                    print(draw(board, path=cur[2], visited=visited))
                return cur[2]
            if n in visited or n not in board or board[n] == "#":
                continue
            if n in keys or n in doors:
                continue
            new_path = collections.deque(cur[2])
            new_path.append(n)
            visited.add(n)
            heap.heappush(h, (cur[0] + 1, n, new_path))
            if draw_search:
                time.sleep(0.0075)
                print(draw(board, keys=keys, doors=doors, path=new_path, visited=visited))
                print(end)
                print(n)

def avail_keys(map: dict, pos: tuple, keys: dict, visited_keys: set, doors: dict, dead=set(), draw_search=False) -> list:
    ''' Return a list of tuples consisting of ( dist, pos ) '''
    visited = set()
    avail = []
    q = collections.deque()
    q.append((0, pos))
    while len(q) != 0:
        cur = q.popleft()
        if cur[1] in keys and keys[cur[1]] not in visited_keys:
            avail.append(cur)
            continue
        for n in neighbours(cur[1]):
            if n in map and map[n] == "#":
                continue
            if n in dead:
                continue
            if n in doors and doors[n].lower() not in visited_keys:
                continue
            if n in visited:
                continue
            visited.add(n)
            q.append((cur[0]+1, n))
            if draw_search:
                print(draw(map, keys=keys, doors=doors, visited=visited, dead=dead))
                print(visited_keys)
                time.sleep(0.01)
    return avail

def avail_keys_doors(map: dict, pos: tuple, keys: dict, doors: dict, dead=set(), draw_search=False) -> list:
    ''' Return a list of tuples consisting of ( dist, pos ) '''
    visited = set()
    avail = []
    q = collections.deque()
    q.append((0, pos))
    while len(q) != 0:
        cur = q.popleft()
        if cur[1] in keys and cur[1] != pos:
            avail.append((cur[0], cur[1], keys[cur[1]]))
            continue
        if cur[1] in doors and cur[1] != pos:
            avail.append((cur[0], cur[1], doors[cur[1]]))
            continue
        for n in neighbours(cur[1]):
            if n in map and map[n] == "#":
                continue
            if n in dead:
                continue
            if n in visited:
                continue
            visited.add(n)
            q.append((cur[0]+1, n))
            if draw_search:
                print(draw(map, keys=keys, doors=doors, visited=visited, dead=dead))
                print(visited_keys)
                time.sleep(0.01)
    return avail

def draw(map, pos=None, keys={}, doors={}, path={}, visited={}, dead=set()) -> str:
    min_x=max_x=min_y=max_y = 0
    for p in map:
        min_x = min(p[0], min_x)
        max_x = max(p[0], max_x)
        min_y = min(p[1], min_y)
        max_y = max(p[1], max_y)
    s = ""
    for y in range(min_y-1, max_y+2):
        s += "\n"
        for x in range(min_x-1, max_x+2):
            point = (x, y)
            if pos is not None and point == pos:
                s += "@"
            elif point in keys:
                s += keys[point]
            elif point in doors:
                s += doors[point]
            elif point in path:
                s += "\u2591"
            elif point in visited:
                s += "."
            elif point in dead:
                s += "X"
            elif point in map:
                if map[point] == "#":
                    s += "\u2588"
                else:
                    s += " "
            else:
                s += "."
    return s

def pos(s, keys, doors):
    for iter in (keys, doors):
        for k, v in keys.items():
            if s == v:
                return k

walls = set()
walkables = set()
map = {}
dead = set()  # dead ends, tiles which are effectivly walls
keys = {}
doors = {}
keys_doors = {}
for y in range(len(f)):
    for x in range(len(f[y].strip())):
        if f[y][x] == "@":
            start = (x,y)
            map[(x,y)] = "."
        elif f[y][x].isalpha():
            if f[y][x].isupper():
                doors[(x,y)] = f[y][x]
                keys_doors[(x,y)] = f[y][x]
            else:
                keys[(x,y)] = f[y][x]
                keys_doors[(x,y)] = f[y][x]
            map[(x,y)] = "?"
        elif f[y][x] == "#":
            map[(x,y)] = "#"
            walls.add((x,y))
        elif f[y][x] == ".":
            map[(x,y)] = "."
            walkables.add((x,y))

for _ in range(10):
    ends = set()
    intersections = set()
    for tile in walkables:
        num_walls = 0
        for n in neighbours(tile):
            if n in walls or n in dead:
                num_walls += 1
        if num_walls == 3:
            ends.add(tile)
        if num_walls < 2:
            intersections.add(tile)

    for end in ends:
        cur = end
        while cur not in intersections and cur not in keys and cur not in doors:
            # is normal point
            dead.add(cur)
            if cur in walkables:
                walkables.remove(cur)
            for n in neighbours(cur):
                if n not in walls and n not in dead:
                    cur = n
                    break

paths = {}
start_paths = {}

# GRAPH: {node: [children as tuples with name and distance]}
graph = {}

for ent, s in keys_doors.items():
    for avail in avail_keys_doors(map, ent, keys, doors, draw_search=False):
        paths[(s, avail[2])] = avail[0]
        graph[s] = graph.get(s, []) + [(avail[2], avail[0])]
used = set()
for path in paths:
    if (path[1], path[0]) in used:
        continue
    print(path[0],"--",path[1])
    used.add((path[0], path[1]))
for avail in avail_keys(map, start, keys, set(), doors):
    start_paths[("@", keys[avail[1]])] = avail[0]
    print("start", "->", keys[avail[1]])

print(graph)
h = []

for path, dist in start_paths.items():
    visited = []
    unlocked = set()
    visited.append(path[1])
    heap.heappush(h, (dist, path[1], visited, unlocked))

m = 0
while True:
    print(cur)
    cur = heap.heappop(h)
    dist = cur[0]
    last = cur[1]
    visited = cur[2]
    unlocked = cur[3]

    if len(unlocked) > m:
        m = len(unlocked)
        print(m, visited)
        if len(unlocked) == len(keys):
            break

    neighbours = graph[last]
    for n in neighbours:
        #TODO recognize cycles
        #if n[0] in visited:
        #    continue
        if n[0].isupper() and n[0] not in unlocked:
            continue
        visited = visited.copy()
        unlocked = unlocked.copy()
        visited.append(n[0])
        if n[0].islower():
            unlocked.add(n[0].upper())
        heap.heappush(h, (dist+n[1], n[0], visited.copy(), unlocked.copy()))
