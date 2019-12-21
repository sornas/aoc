# program and idea for part 1:
# jump if any tile of the first three aren't ground and the fourth is ground
# J = (not A or not B or not C) and D
# (dm) <=> J = not (A and B and C) and D
# or A T
# and B T
# and C T
# not T J
# and D J
# walk

import intcode

f = open("../input/21", "r").readlines()

c = intcode.Computer([int(x) for x in f[0].split(",")], ascii=True)
output = []

def ascii_draw(a):
    s = ""
    for c in a:
        if c == 10:
            s += "\n"
        elif c < 128:
            s += chr(c)
        else:
            print("[INVALID ASCII]", c)
    return s

while not c.SIG_HALT:
    c.step()
    if c.SIG_INPUT:
        # flush output
        print(ascii_draw(output))
        output = []
        if len(output) > 0:
            output = []
        while True:
            s = input()
            if s.upper() == "END":
                break
            c.queue_ascii(s.upper())
    if c.SIG_OUTPUT:
        output.append(c.output)
        c.output = None
print(output)
print(ascii_draw(output))
