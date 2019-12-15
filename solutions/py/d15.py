import intcode
import heapq as heap
import collections
import queue
import time

size = 2
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
                s += "D" * size
            elif path is not None and point in path:
                s += "\u2591" * size
            elif visited is not None and point in visited:
                s += "." * size
            elif point in board:
                if board[point] == "#":
                    s += "\u2588" * size
                elif board[point] == "S":
                    s += "\u2591" * size
                else:
                    s += " " * size
            else:
                s += "." * size
    return s

def neighbours(p):
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), \
            (p[0], p[1]+1), (p[0], p[1]-1)]

def get_path(start, end, board):
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
                return cur[2]
            if n in visited:
                continue
            if n not in board:
                continue
            if board[n] == "#":
                continue
            new_path = collections.deque(cur[2])
            new_path.append(n)
            visited.add(n)
            #print(draw(board, path=new_path, visited=visited))
            #time.sleep(0.01)
            heap.heappush(h, (cur[0] + 1, n, new_path))

cur_x = cur_y = 0
stack = collections.deque()
stack.append((0,0))
path = collections.deque()
board = {}
oxygen = (0,0)

f = open("../input/15", "r").readlines()
c = intcode.Computer([int(x) for x in f[0].split(",")])

auto = True
steps = 0
while not c.SIG_HALT:
    if auto and len(stack) == 0:
        print("stack empty")
        break
    c.step()
    if c.SIG_INPUT:
        direction = 0
        prev_x, prev_y = cur_x, cur_y
        if auto:
            if len(path) == 0:
                # find new path
                for n in neighbours((cur_x, cur_y)):
                    if n not in stack and n not in board:
                        stack.append(n)
                next = stack.pop()
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
        else:  # manual
            next_step = input()
            if next_step == "w":
                direction = 1
                cur_y -= 1
            elif next_step == "s":
                direction = 2
                cur_y += 1
            elif next_step == "a":
                direction = 3
                cur_x -= 1
            elif next_step == "d":
                direction = 4
                cur_x += 1
            else:
                continue
        c.input = direction
        steps += 1
        c.SIG_INPUT = False
    if c.SIG_OUTPUT:
        # time.sleep(0.075)
        # print(draw(board, droid=(cur_x, cur_y)))
        if c.output == 0:
            board[(cur_x, cur_y)] = "#"
            cur_x, cur_y = prev_x, prev_y
        elif c.output == 1:
            board[(cur_x, cur_y)] = "."
        elif c.output == 2:
            board[(cur_x, cur_y)] = "S"
            print("found oxygen at", (cur_x, cur_y))
            oxygen = (cur_x, cur_y)
        else:
            break
        c.output = None
        c.SIG_OUTPUT = False
        if not auto:
            print(draw(board, (cur_x, cur_y)))
print(draw(board))
print(draw(board, path=get_path((0,0), oxygen, board)))
print(len(get_path((0,0), oxygen, board)))
print(steps)
