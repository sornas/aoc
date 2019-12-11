import intcode
import time


def draw(colors, ship, direction):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    ship_c = ""
    if direction == 0:
        ship_c = "^"
    elif direction == 1:
        ship_c = "<"
    elif direction == 2:
        ship_c = "v"
    elif direction == 3:
        ship_c = ">"
    for color in colors:
        min_x = min(min_x, color[0])
        max_x = max(max_x, color[0])
        min_y = min(min_y, color[1])
        max_y = max(max_y, color[1])
    s = ""
    for y in range(min_y-1, max_y+2):
        s += "\n"
        for x in range(min_x-1, max_x+1):
            if (x,y) == ship:
                s += ship_c
            elif (x,y) in colors:
                c = colors[(x,y)]
                s += "\u2588" if c == 1 else " "
            else:
                s += "."
    return s

def pt1(input):
    program = [int(x) for x in input[0].split(",")]
    x=y = 0
    direction = 0
    # 0 is up
    # 1 is left
    # 2 is down
    # 3 is right
    # 4 is up (again)
    # turning left is direction += 1
    # turning right is direction -= 1
    # direction is direction % 4
    colors = {}  # (x,y): 1/0 (1 = white, 0 = black)

    got_color = False
    c = intcode.Computer(program)
    while c.memory[c.pointer] != 99:
        # input
        #print(x, y)
        #draw(colors, (x,y), direction % 4)
        #input()
        #time.sleep(0.1)
        c.input = colors.get((x, y), 0)
        c.step()
        if c.output is not None:
            if not got_color:
                colors[(x, y)] = c.output
                c.output = None
                got_color = True
            elif got_color:
                direction += (1 if c.output == 0 else -1)
                dir = direction % 4
                if dir == 0:
                    y -= 1
                elif dir == 1:
                    x -= 1
                elif dir == 2:
                    y += 1
                elif dir == 3:
                    x += 1
                got_color = False
                c.output = None
    return len(colors)

def pt2(input):
    program = [int(x) for x in input[0].split(",")]
    x=y = 0
    direction = 0
    # 0 is up
    # 1 is left
    # 2 is down
    # 3 is right
    # 4 is up (again)
    # turning left is direction += 1
    # turning right is direction -= 1
    # direction is direction % 4
    colors = {(0,0): 1}  # (x,y): 1/0 (1 = white, 0 = black)

    got_color = False
    c = intcode.Computer(program)
    while c.memory[c.pointer] != 99:
        c.input = colors.get((x, y), 0)
        c.step()
        if c.output is not None:
            if not got_color:
                colors[(x, y)] = c.output
                c.output = None
                got_color = True
            elif got_color:
                direction += (1 if c.output == 0 else -1)
                dir = direction % 4
                if dir == 0:
                    y -= 1
                elif dir == 1:
                    x -= 1
                elif dir == 2:
                    y += 1
                elif dir == 3:
                    x += 1
                got_color = False
                c.output = None
    return draw(colors, (0,0), 0)

def visualize(input):
    program = [int(x) for x in input[0].split(",")]
    x=y = 0
    direction = 0
    # 0 is up
    # 1 is left
    # 2 is down
    # 3 is right
    # 4 is up (again)
    # turning left is direction += 1
    # turning right is direction -= 1
    # direction is direction % 4
    colors = {(0,0): 1}  # (x,y): 1/0 (1 = white, 0 = black)

    got_color = False
    c = intcode.Computer(program)
    while c.memory[c.pointer] != 99:
        time.sleep(0.002)
        print(draw(colors, (x,y), direction % 4))
        c.input = colors.get((x, y), 0)
        c.step()
        if c.output is not None:
            if not got_color:
                colors[(x, y)] = c.output
                c.output = None
                got_color = True
            elif got_color:
                direction += (1 if c.output == 0 else -1)
                dir = direction % 4
                if dir == 0:
                    y -= 1
                elif dir == 1:
                    x -= 1
                elif dir == 2:
                    y += 1
                elif dir == 3:
                    x += 1
                got_color = False
                c.output = None

if __name__ == "__main__":
    import cProfile

    input = open("../input/11", "r").readlines()
    cProfile.run("pt1(input)")
    cProfile.run("pt2(input)")
    print(pt1(input))
    print(pt2(input))
    visualize(input)
