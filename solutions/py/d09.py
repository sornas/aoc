import intcode

input = open("../input/09", "r").readlines()[0]

program = [int(x) for x in input.split(",")]
c = intcode.Computer(program)
c.input = 2
while c.memory[c.pointer] != 99:
    c.step()
    #print(c.relative_base, c.pointer, c.memory)
    if c.output is not None:
        print(c.output)
        c.output = None
