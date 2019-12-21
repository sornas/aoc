import collections
import heapq as heap
import sys

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

def avail(map, start, items, dead, ignore=set(), ignore_except=set()):
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
            if n in ignore and n not in ignore_except:
                continue
            if n in map and map[n] == "#":
                continue
            if n in dead:
                continue
            if n in visited:
                continue
            visited.add(n)
            q.append((dist+1, n))
    return avail

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
for a in avail(map, start, map_keys, dead, map_doors):
    start_paths[("@", map_keys[a[1]])] = a[0]

def v_from_k(items: dict, item: str):
    for k,v in items.items():
        if item == v:
            return k
    return None

def pos_from_item(item, keys, doors):
    return v_from_k((keys if item.islower() else doors), item)

def avail_keys(map, keys, doors, graph, start, keys_left, unlocked_doors):
    visited = set()
    avail = []
    h = []
    heap.heappush(h, (0, start))
    while len(h) > 0:
        dist, cur_key = heap.heappop(h)
        if cur_key != start and cur_key.islower() and cur_key in keys_left:
            avail.append((dist, cur_key))
            continue
        for n in graph[cur_key]:
            if n[0].isupper() and n[0] not in unlocked_doors:
                continue
            if n[0] in visited:
                continue
            visited.add(n[0])
            heap.heappush(h, (dist + n[1], n[0]))
    return avail

h = []

for path, dist in start_paths.items():
    cur = path[1]
    keys_left = set(map_keys.values()).copy()
    keys_left.remove(cur)
    unlocked = set()
    unlocked.add(cur.upper())
    key_path = [cur]
    heap.heappush(h, (dist, cur, keys_left, unlocked, key_path))

best = len(map_keys)
seen = set()

while True:
    dist, key, keys_left, unlocked, key_path = heap.heappop(h)
    #print("\nnode", dist, key, keys_left, unlocked, key_path)
    if (frozenset(key_path), key) in seen:
        #print("skipping", key_path, key)
        continue
    seen.add((frozenset(key_path), key))
    if len(keys_left) == 0:
        print(dist, "with path", key_path)
        sys.exit()
    if len(keys_left) < best:
        best = len(keys_left)
        print("best", len(unlocked), "with dist", dist, "and path", key_path)
    for new_dist, new_key in avail_keys(map, map_keys, map_doors, graph, key, keys_left, unlocked):
        #print("edge", new_dist, new_key)
        new_keys_left = keys_left.copy()
        new_keys_left.remove(new_key)
        new_unlocked = unlocked.copy()
        new_unlocked.add(new_key.upper())
        new_key_path = key_path.copy()
        new_key_path.append(new_key)
        #print("adding", dist+new_dist, new_key, new_keys_left, new_unlocked, new_key_path)
        heap.heappush(h, (dist + new_dist, new_key, new_keys_left, new_unlocked, new_key_path))
