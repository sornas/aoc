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

jumpscript = open("21.js", "r").readlines()
for line in jumpscript:
    if line[0] != "#":
        c.queue_ascii(line.strip().upper())
        print(line.strip().upper())

while not c.SIG_HALT:
    c.step()
    if c.SIG_OUTPUT:
        output.append(c.output)
        c.output = None
print(output)
print(ascii_draw(output))
