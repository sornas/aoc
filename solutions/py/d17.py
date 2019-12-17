import intcode
from collections import deque
import heapq as heap
import time

def draw(view, intersections={}, robot=None, direction=None):
    min_x=max_x=min_y=max_y = 0
    for p in view:
        min_x = min(p[0], min_x)
        max_x = max(p[0], max_x)
        min_y = min(p[1], min_y)
        max_y = max(p[1], max_y)
    s = ""
    for y in range(min_y, max_y+1):
        s += "\n"
        for x in range(min_x, max_x+1):
            point = (x, y)
            if robot is not None and point == robot:
                if direction == 0:
                    s += ">"
                elif direction == 1:
                    s += "v"
                elif direction == 2:
                    s += "<"
                elif direction == 3:
                    s += "^"
                else:
                    s += "D"
            elif point in intersections:
                s += "O"
            elif point in view:
                s += view[point] * 1
            else:
                s += " " * 1
    return s

def neighbours(p):
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), \
            (p[0], p[1]+1), (p[0], p[1]-1)]

c = intcode.Computer([int(x) for x in open("../input/17", "r").readlines()[0].split(",")])

view = {}
scaffolds = []
buffer = ""
x=y = 0
while not c.SIG_HALT:
    c.step()
    if c.SIG_INPUT:
        print("input??")
        break
    if c.SIG_OUTPUT:
        if c.output == 10:
            y += 1
            x = 0
        elif c.output == 35:
            view[(x,y)] = "#"
            scaffolds.append((x,y))
            x += 1
        elif c.output == 46:
            view[(x,y)] = "."
            x += 1
        else:
            view[(x,y)] = "#"
            scaffolds.append((x,y))
            robot = (x,y)
            if c.output == 60:  # <
                direction = 2
            elif c.output == 62:  # >
                direction = 0
            elif c.output == 94:  # ^
                direction = 3
            elif c.output == 86 or c.output == 118:  # V or v
                direction = 1
            else:
                print("????????????????")
                break
            x += 1
        buffer = ""
        c.output = None
        c.SIG_OUTPUT = False
print(draw(view))

intersections =  set()
al_sum = 0
for s in scaffolds:
    ns = 0
    for n in neighbours(s):
        if n in scaffolds:
            ns += 1
    if ns == 4:
        intersections.add(s)
        al_sum += s[0] * s[1]
print(intersections)
print(draw(view, intersections=intersections, robot=robot, direction=direction))
print(al_sum)

x,y = robot
visited = set()
left = set()
for s in scaffolds:
    left.add(s)

def get_infront(robot, direction):
    dx=dy = 0
    if direction == 0:
        dx = 1
    elif direction == 1:
        dy = 1
    elif direction == 2:
        dx = -1
    else:
        dy = -1
    return (robot[0]+dx, robot[1]+dy)

def get_behind(robot, direction):
    dx=dy = 0
    if direction == 0:
        dx = -1
    elif direction == 1:
        dy = -1
    elif direction == 2:
        dx = 1
    else:
        dy = 1
    return (robot[0]+dx, robot[1]+dy)

def get_turn(robot, direction, point):
    dx = point[0] - robot[0]
    dy = point[1] - robot[1]
    if dx == 1:
        turn_direction = 0
    elif dy == 1:
        turn_direction = 1
    elif dx == -1:
        turn_direction = 2
    else:
        turn_direction = 3
    if direction == turn_direction:
        return None
    if (direction + 1) % 4 == turn_direction:
        return "R"
    elif (direction - 1) % 4 == turn_direction:
        return "L"
    else:
        return False

def get_direction(direction, turn):
    if turn == "L":
        return (direction - 1) % 4
    elif turn == "R":
        return (direction + 1) % 4
    else:
        return False

def get_turnable_points(scaffolds, robot, direction):
    valid = set()
    for n in neighbours(robot):
        if n in scaffolds and n != get_behind(robot, direction):
            valid.add(n)
    return list(valid)

'''
For each path, take steps until a wall is reached. For each intersection on the
way, queue new searches with turns (but don't start them, FIFO). When a wall is
reached, check if each point has been visited. If all points have been visited,
done. Else, 

Structure of a deque-element:
Each search-element consists of a single tuple. The tuple contains
  - The robot's position
  - The robot's direction (after turning)
  - The instruction-set up to that point
  - The current WIP instruction
  - All points that have been visited (as a set)

Structure of the instruction-set:
The instruction-set consists of a list of tuples. The tuples contain
  - A turn-instruction
  - The number of steps to take (after turning)
For example:
[(R,8), (R,8), (R,4), (R,4), (R,8)]
'''

current = None
direction = 2
paths = deque()
visited = set()
visited.add(robot)
paths.append((robot, direction, [], ["L", 0], visited))
while True:
    if current is None:
        current = paths.popleft()
        robot = current[0]
        direction = current[1]
        instruction_set = current[2]
        wip_instruction = current[3]
        visited = current[4].copy()
        if len(visited) == len(scaffolds):
            print("len(visited) == len(scaffolds)")
            instruction_set.append(wip_instruction)
            break
    if get_infront(robot, direction) not in scaffolds:
        # wall in front. save
        instruction_set.append(wip_instruction)
        avail_points = get_turnable_points(scaffolds, robot, direction)
        if len(avail_points) == 0:
            if len(visited) == len(scaffolds):
                break
            else:
                current = None
                continue
        wip_instruction = [get_turn(robot, direction, avail_points[0]), 0]
        direction = get_direction(direction, get_turn(robot, direction, avail_points[0]))
        paths.append((robot, direction, instruction_set, wip_instruction, visited))
        current = None
    else:  # wall not in front
        '''
        if robot in intersections and wip_instruction[1] != 0:
            # queue intersections
            new_instruction_set = instruction_set.copy()
            new_instruction_set.append(wip_instruction.copy())
            paths.append((robot, get_direction(direction, "L"), \
                    new_instruction_set.copy(), ["L", 0], visited))
            paths.append((robot, get_direction(direction, "R"), \
                    new_instruction_set.copy(), ["R", 0], visited))
                    '''
        # take step
        robot = get_infront(robot, direction)
        visited.add(robot)
        wip_instruction[1] += 1

print(instruction_set)
s = ""
for instruction in instruction_set:
    s += str(instruction[0]) + "," + str(instruction[1]) + "\n"
print(s)

main_routine = "A,A,B,C,C,A,C,B,C,B"
routine_a = "L,4,L,4,L,6,R,10,L,6"
routine_b = "L,12,L,6,R,10,L,6"
routine_c = "R,8,R,10,L,6"

msg = deque()
for s in [main_routine, routine_a, routine_b, routine_c]:
    for ch in s:
        msg.append(ord(ch))
    msg.append(10)
msg.append(ord("n"))
msg.append(10)
print(msg)

c.reset()
c.memory[0] = 2
while not c.SIG_HALT:
    c.step()
    if c.SIG_INPUT:
        c.input = msg.popleft()
        c.SIG_INPUT = False
    if c.SIG_OUTPUT:
        print(c.output)
        c.output = None
        c.SIG_OUTPUT = False
