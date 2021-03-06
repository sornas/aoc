import intcode

def do(input, code):
    program = [int(x) for x in input.split(",")]
    c = intcode.Computer(program)
    c.input = code
    output = []
    while True:
        c.step()
        #print(c.relative_base, c.pointer, c.memory)
        if c.SIG_HALT:
            break
        if c.output is not None:
            output.append(c.output)
            c.output = None
    return output

def pt1(input):
    return do(input[0], 1)

def pt2(input):
    return do(input[0], 2)

if __name__ == "__main__":
    input = open("../input/09", "r").readlines()
    print(pt1(input))
    print(pt2(input))
