import intcode

def ascii_draw(a):
    s = ""
    post = ""
    for c in a:
        if c == 10:
            s += "\n"
        elif c < 128:
            s += chr(c)
        else:
            post = "[INVALID ASCII]: " + str(c)
    return s + ("\n" if post != "" else "") + post

def do(c, jumpscript):
    output = []
    for line in jumpscript:
        if line[:2] != "//":
            c.queue_ascii(line.strip().upper())
    while not c.SIG_HALT:
        c.step()
        if c.SIG_OUTPUT:
            output.append(c.output)
            c.output = None
    return ascii_draw(output)

def pt1(input):
    c = intcode.Computer([int(x) for x in input[0].split(",")], ascii=True)
    return do(c, open("21-1.js", "r").readlines())

def pt2(input):
    c = intcode.Computer([int(x) for x in input[0].split(",")], ascii=True)
    return do(c, open("21-2.js", "r").readlines())

if __name__ == "__main__":
    input = open("../input/21", "r").readlines()
    print(pt1(input))
    print(pt2(input))
