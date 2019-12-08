import intcode

def pt1(input):
    program = [int(x) for x in input[0].split(",")]
    c = intcode.Computer(program)
    c.input = 1
    output = []
    while c.memory[c.pointer] != 99:
        c.step()
        if c.output != None:
            output.append(c.output)
            c.output = None
    return output

def pt2(input):
    program = [int(x) for x in input[0].split(",")]
    c = intcode.Computer(program)
    c.input = 5
    output = []
    while c.memory[c.pointer] != 99:
        c.step()
        if c.output != None:
            output.append(c.output)
            c.output = None
    return output

