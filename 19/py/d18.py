import collections
import heapq as heap

def neighbours(p):
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), \
            (p[0], p[1]+1), (p[0], p[1]-1)]

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

def avail(map, start, items, dead):
    visited = set()
    avail = []
    q = collections.deque()
    q.append((0, start))
    while len(q) > 0:
        cur = q.popleft()
        dist = cur[0]
        pos = cur[1]
        if pos in items and pos != start:
            avail.append((dist, pos, items[pos]))
            continue
        for n in neighbours(pos):
            if n in map and map[n] == "#":
                continue
            if n in dead:
                continue
            if n in visited:
                continue
            visited.add(n)
            q.append((dist+1, n))
    return avail

def seen_before(keys, paths):
    for path in paths:
        if set(keys) == set(path) and keys[-1] == path[-1]:
            return True
    return False

input = open("../input/18", "r").readlines()

map = {}
map_keys = {}
map_doors = {}
map_keys_doors = {}
walls = set()
tiles = set()

for y in range(len(input)):
    for x in range(len(input[y].strip())):
        c = input[y][x]
        p = (x,y)
        if c == "@":
            start = p
            map[p] = "."
        elif c.isalpha():
            if c.isupper():
                map_doors[p] = c
            else:
                map_keys[p] = c
            map[p] = "."
        elif c == "#":
            walls.add(p)
            map[p] = c
        elif c == ".":
            tiles.add(p)
            map[p] = c
map_keys_doors.update(map_keys)
map_keys_doors.update(map_doors)

dead = set()
for _ in range(10):
    ends = set()
    intersections = set()
    for tile in tiles:
        num_walls = 0
        for n in neighbours(tile):
            if n in walls or n in dead:
                num_walls += 1
        if num_walls == 3:
            ends.add(tile)
        elif num_walls < 2:
            intersections.add(tile)
    
    for end in ends:
        cur = end
        while cur not in intersections and cur not in map_keys and cur not in map_doors:
            dead.add(cur)
            if cur in tiles:
                tiles.remove(cur)
            for n in neighbours(cur):
                if n not in walls and n not in dead:
                    cur = n
                    break
paths = {}  # every path available between a door and a key
start_paths = {}  # every path available from the starting point

graph = {}  # {node: [children as tuples with name and distance]}
for ent, s in map_keys_doors.items():
    for a in avail(map, ent, map_keys_doors, dead):
        paths[(s, a[2])] = a[0]
        graph[s] = graph.get(s, []) + [(a[2], a[0])]
for a in avail(map, start, map_keys, dead):
    start_paths[("@", map_keys[a[1]])] = a[0]

h = []

for path, dist in start_paths.items():
    cur = path[1]
    keys = [path[1]]
    unlocked = set()
    unlocked.add(cur.upper())
    heap.heappush(h, (dist, cur, keys, unlocked))

m = 0
seen = []

while True:
    print(len(h))
    candidate = heap.heappop(h)
    dist = candidate[0]
    cur = candidate[1]
    keys = candidate[2]
    unlocked = candidate[3]

    # if seen_before
    if seen_before(keys, seen):
        continue
    seen.append(keys)

    if len(unlocked) > m:
        m = len(unlocked)
        print(m, keys)
        if len(unlocked) == len(map_doors):
            break
    
    for n in graph[cur]:
        if n[0].isupper() and n[0] not in unlocked:
            continue
        keys = keys.copy()
        unlocked = unlocked.copy()
        if n[0].islower():
            keys.append(n[0])
            unlocked.add(n[0].upper())
        heap.heappush(h, (dist+n[1], n[0], keys, unlocked))
