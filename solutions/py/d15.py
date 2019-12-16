import intcode
import heapq as heap
import collections
import time

def neighbours(p):
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), \
            (p[0], p[1]+1), (p[0], p[1]-1)]

def get_path(start, end, board, draw_search=False):
    if start == end:
        return collections.deque()
    visited = set()
    h = []
    heap.heappush(h, (0, start, collections.deque()))
    while True:
        cur = heap.heappop(h)
        for n in neighbours(cur[1]):
            if n == end:
                cur[2].append(n)
                if draw_search:
                    print(draw(board, path=cur[2], visited=visited))
                return cur[2]
            if n in visited or n not in board or board[n] == "#":
                continue
            new_path = collections.deque(cur[2])
            new_path.append(n)
            visited.add(n)
            heap.heappush(h, (cur[0] + 1, n, new_path))
            if draw_search:
                time.sleep(0.005)
                print(draw(board, path=new_path, visited=visited))

def pt1(input):
    cur_x = cur_y = 0
    q = collections.deque()
    q.append((0,0))
    path = collections.deque()
    board = {}
    board[(0,0)] = "."

    c = intcode.Computer([int(x) for x in input[0].split(",")])

    while not c.SIG_HALT:
        if len(q) == 0:
            break
        c.step()
        if c.SIG_INPUT:
            direction = 0
            prev_x, prev_y = cur_x, cur_y
            if len(path) == 0:
                # find new path
                for n in neighbours((cur_x, cur_y)):
                    if n not in q and n not in board:
                        q.append(n)
                if (cur_x, cur_y) in q:
                    q.remove((cur_x, cur_y))
                next = q.pop()
                path = get_path((cur_x, cur_y), next, board)
            next_step = path.popleft()
            if next_step[1] == cur_y-1:
                direction = 1
                cur_y -= 1
            elif next_step[1] == cur_y+1:
                direction = 2
                cur_y += 1
            elif next_step[0] == cur_x-1:
                direction = 3
                cur_x -= 1
            elif next_step[0] == cur_x+1:
                direction = 4
                cur_x += 1
            else:
                print("invalid path")
                break
            c.input = direction
            c.SIG_INPUT = False
        if c.SIG_OUTPUT:
            if c.output == 0:
                board[(cur_x, cur_y)] = "#"
                cur_x, cur_y = prev_x, prev_y
            elif c.output == 1:
                board[(cur_x, cur_y)] = "."
            elif c.output == 2:
                board[(cur_x, cur_y)] = "S"
                oxygen = (cur_x, cur_y)
            else:
                break
            c.output = None
            c.SIG_OUTPUT = False
    return len(get_path((0,0), oxygen, board))

def pt2(input):
    cur_x = cur_y = 0
    q = collections.deque()
    q.append((0,0))
    path = collections.deque()
    board = {}
    board[(0,0)] = "."
    oxygen = (0,0)

    c = intcode.Computer([int(x) for x in input[0].split(",")])

    while not c.SIG_HALT:
        if len(q) == 0:
            break
        c.step()
        if c.SIG_INPUT:
            direction = 0
            prev_x, prev_y = cur_x, cur_y
            if len(path) == 0:
                # find new path
                for n in neighbours((cur_x, cur_y)):
                    if n not in q and n not in board:
                        q.append(n)
                if (cur_x, cur_y) in q:
                    q.remove((cur_x, cur_y))
                next = q.pop()
                path = get_path((cur_x, cur_y), next, board)
            next_step = path.popleft()
            if next_step[1] == cur_y-1:
                direction = 1
                cur_y -= 1
            elif next_step[1] == cur_y+1:
                direction = 2
                cur_y += 1
            elif next_step[0] == cur_x-1:
                direction = 3
                cur_x -= 1
            elif next_step[0] == cur_x+1:
                direction = 4
                cur_x += 1
            else:
                print("invalid path")
                break
            c.input = direction
            c.SIG_INPUT = False
        if c.SIG_OUTPUT:
            if c.output == 0:
                board[(cur_x, cur_y)] = "#"
                cur_x, cur_y = prev_x, prev_y
            elif c.output == 1:
                board[(cur_x, cur_y)] = "."
            elif c.output == 2:
                board[(cur_x, cur_y)] = "S"
                oxygen = (cur_x, cur_y)
            else:
                break
            c.output = None
            c.SIG_OUTPUT = False

    steps = 0
    visited = set(oxygen)
    cur_layer = []
    next_layer = [oxygen]
    while True:
        cur_layer = next_layer.copy()
        next_layer = []
        for p in cur_layer:
            for n in neighbours(p):
                if n in board and board[n] != "#" and n not in visited:
                    visited.add(n)
                    next_layer.append(n)
        if len(next_layer) == 0:
            break
        steps += 1
    return steps

def draw(board, droid=None, path=None, visited=None):
    min_x=max_x=min_y=max_y = 0
    for p in board:
        min_x = min(p[0], min_x)
        max_x = max(p[0], max_x)
        min_y = min(p[1], min_y)
        max_y = max(p[1], max_y)
    s = ""
    for y in range(min_y-1, max_y+2):
        s += "\n"
        for x in range(min_x-1, max_x+2):
            point = (x, y)
            if droid is not None and point == droid:
                s += "D" * 2
            elif path is not None and point in path:
                s += "\u2591" * 2
            elif visited is not None and point in visited:
                s += "." * 2
            elif point in board:
                if board[point] == "#":
                    s += "\u2588" * 2
                elif board[point] == "S":
                    s += "\u2591" * 2
                else:
                    s += " " * 2
            else:
                s += "." * 2
    return s

def visualize(input):
    cur_x = cur_y = 0
    q = collections.deque()
    q.append((0,0))
    path = collections.deque()
    board = {}
    board[(0,0)] = "."

    c = intcode.Computer([int(x) for x in input[0].split(",")])

    while not c.SIG_HALT:
        if len(q) == 0:
            break
        c.step()
        if c.SIG_INPUT:
            direction = 0
            prev_x, prev_y = cur_x, cur_y
            if len(path) == 0:
                # find new path
                for n in neighbours((cur_x, cur_y)):
                    if n not in q and n not in board:
                        q.append(n)
                if (cur_x, cur_y) in q:
                    q.remove((cur_x, cur_y))
                next = q.pop()
                path = get_path((cur_x, cur_y), next, board)
            next_step = path.popleft()
            if next_step[1] == cur_y-1:
                direction = 1
                cur_y -= 1
            elif next_step[1] == cur_y+1:
                direction = 2
                cur_y += 1
            elif next_step[0] == cur_x-1:
                direction = 3
                cur_x -= 1
            elif next_step[0] == cur_x+1:
                direction = 4
                cur_x += 1
            else:
                print("invalid path")
                break
            c.input = direction
            c.SIG_INPUT = False
        if c.SIG_OUTPUT:
            if c.output == 0:
                board[(cur_x, cur_y)] = "#"
                cur_x, cur_y = prev_x, prev_y
            elif c.output == 1:
                board[(cur_x, cur_y)] = "."
            elif c.output == 2:
                board[(cur_x, cur_y)] = "S"
                oxygen = (cur_x, cur_y)
            else:
                break
            time.sleep(0.0075)
            print(draw(board, droid=(cur_x, cur_y)))
            c.output = None
            c.SIG_OUTPUT = False

    get_path((0,0), oxygen, board, draw_search=True)

    steps = 0
    visited = set(oxygen)
    cur_layer = []
    next_layer = [oxygen]
    while True:
        cur_layer = next_layer.copy()
        next_layer = []
        for p in cur_layer:
            for n in neighbours(p):
                if n in board and board[n] != "#" and n not in visited:
                    visited.add(n)
                    next_layer.append(n)
        if len(next_layer) == 0:
            break
        steps += 1

if __name__ == "__main__":
    input = open("../input/15", "r").readlines()
    print(pt1(input))
    print(pt2(input))
    visualize(input)
