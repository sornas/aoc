import collections
import intcode
import sys
import time

def draw(beam):
    min_x=max_x=min_y=max_y = 0
    for p in beam:
        min_x = min(p[0], min_x)
        max_x = max(p[0], max_x)
        min_y = min(p[1], min_y)
        max_y = max(p[1], max_y)
    s = ""
    for y in range(min_y, max_y+1):
        s += "\n"
        for x in range(min_x, max_x+1):
            point = (x,y)
            if point in beam:
                s += "#" if beam[point] else " "
            else:
                s += "?"
    return s

def deploy(c, x, y):
    c.reset()
    input = collections.deque((x,y))
    while True:
        c.step()
        if c.SIG_INPUT:
            c.input = input.popleft()
        if c.SIG_OUTPUT:
            break
    return c.output

def do(input):
    amount = 0
    c = intcode.Computer([int(x) for x in input[0].split(",")])

    #                     ####      46
    #                      ####     47
    #                       ####    48
    #                       #####   49
    #                        ####   50

    # assume every row has a point. this can be done by starting from row 50
    # (or some other larger enough number)

    # search each row one by one. when the lenght of the row has been
    # determined, check the length of the col of every point where the distance
    # to the right is greater than 100. if no col longer than 100 is found,
    # skip to the next row (and check only starting from the same x as the
    # first x of the row above)

    y = 1000  # tested to not be 100 until after row 1000
    start_x = 0
    while True:
        found = False
        x = start_x
        amount_in_row = 0
        while True:
            if deploy(c, x, y) == 1:
                if not found:
                    start_x = x
                    found = True
                amount_in_row += 1
            elif found:
                break
            x += 1
        tries = amount_in_row - 100
        for i in range(0, tries+1):
            # check downwards
            amount_in_col = 0
            row = y
            while True:
                if deploy(c, start_x+i, row) == 1:
                    amount_in_col += 1
                    row += 1
                else:
                    break
            if amount_in_col >= 100:
                # done
                return start_x+i, y 
        y += 1

input = open("../input/19", "r").readlines()
print(do(input))
