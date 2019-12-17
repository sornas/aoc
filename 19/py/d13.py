import intcode
import queue
import time

def pt1(input):
    c = intcode.Computer([int(x) for x in input[0].split(",")])
    buffer_out = []
    screen = {}
    while c.memory[c.pointer] != 99:
        c.step()
        if c.output is not None:
            buffer_out.append(c.output)
            c.output = None
        if len(buffer_out) == 3:
            screen[(buffer_out[0], buffer_out[1])] = buffer_out[2]
            buffer_out = []
    blocks = 0
    for p in screen:
        if screen[p] == 2:
            blocks += 1
    return blocks


def pt2(input):
    def draw(screen, points):
        ball_x = 0
        paddle_x = 0
        min_x = max_x = min_y = max_y = 0
        for p in screen:
            if p == (-1,0):
                points = screen[p]
            elif screen[p] == 3:
                paddle_x = p[0]
            elif screen[p] == 4:
                ball_x = p[0]
        return points, ball_x, paddle_x

    c = intcode.Computer([int(x) for x in input[0].split(",")])
    c.memory[0] = 2

    screen = {}
    buffer_out = []
    points = 0
    ball_x = paddle_x = 0

    while c.memory[c.pointer] != 99:
        if c.SIG_INPUT:
            points, ball_x, paddle_x = draw(screen, points)
            if paddle_x < ball_x:
                c.input = 1
            elif paddle_x > ball_x:
                c.input = -1
            else:
                c.input = 0
        c.step()
        if c.output is not None:
            buffer_out.append(c.output)
            c.output = None
        if len(buffer_out) == 3:
            screen[(buffer_out[0], buffer_out[1])] = buffer_out[2]
            buffer_out = []
    return c.memory[386]

def visualize(input):
    def draw(screen, points):
        ball_x = 0
        paddle_x = 0
        min_x = max_x = min_y = max_y = 0
        for p in screen:
            min_x = min(min_x, p[0])
            max_x = max(max_x, p[0])
            min_y = min(min_y, p[1])
            max_y = max(max_y, p[1])
        s = ""
        for y in range(min_y-1, max_y+1):
            for x in range(min_x-1, max_x+1):
                if (x,y) in screen:
                    if (x,y) == (-1,0):
                        points = screen[(x,y)]
                    elif screen[(x,y)] == 0:
                        s += " "
                    elif screen[(x,y)] == 1:
                        s += "\u2588"
                    elif screen[(x,y)] == 2:
                        s += "#"
                    elif screen[(x,y)] == 3:
                        s += "-"
                        paddle_x = x
                    elif screen[(x,y)] == 4:
                        s += "O"
                        ball_x = x
                else:  # (x,y) not in screen
                    s += " "
            s += "\n"
        return s, points, ball_x, paddle_x

    c = intcode.Computer([int(x) for x in input[0].split(",")])
    c.memory[0] = 2

    screen = {}
    buffer_out = []
    frame_n = 0
    points = 0
    ball_x = paddle_x = 0

    while c.memory[c.pointer] != 99:
        if c.SIG_INPUT:
            time.sleep(0.01)
            frame_n += 1
            frame, points, ball_x, paddle_x = draw(screen, points)
            print(frame)
            if paddle_x < ball_x:
                c.input = 1
            elif paddle_x > ball_x:
                c.input = -1
            else:
                c.input = 0
        c.step()
        if c.output is not None:
            buffer_out.append(c.output)
            c.output = None
        if len(buffer_out) == 3:
            screen[(buffer_out[0], buffer_out[1])] = buffer_out[2]
            buffer_out = []

if __name__ == "__main__":
    import cProfile

    _input = open("../input/13", "r").readlines()
    print(pt1(_input))
    print(pt2(_input))
    #visualize(_input)
