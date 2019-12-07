import intcode
import itertools
import queue
import sys

def pt1(program):
    c = intcode.Computer(program)
    c.input = 1
    output = []
    while c.memory[c.pointer] != 99:
        c.step()
        if c.output != None:
            output.append(c.output)
            c.output = None
    return output

def pt2(program):
    c = intcode.Computer(program)
    c.input = 5
    output = []
    while c.memory[c.pointer] != 99:
        c.step()
        if c.output != None:
            output.append(c.output)
            c.output = None
    return output

if __name__ == "__main__":
    f = open("../input/05", "r")
    program = [int(x) for x in f.readline().split(",")]

    import cProfile
    import timeit

    print("PART 1")
    print(timeit.timeit('pt1(program)', globals=globals(), number=1000), "ms")
    cProfile.run("pt1(program)")

    print("PART 2")
    print(timeit.timeit('pt2(program)', globals=globals(), number=1000), "ms")
    cProfile.run("pt2(program)")

    print(1, pt1(program))
    print(2, pt2(program))
