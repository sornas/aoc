import sys

def pt1(input):
    program = [int(x) for x in input[0].split(",")]

    memory = program.copy()
    memory[1] = 12
    memory[2] =  2

    pointer = 0
    while True:
        if memory[pointer] == 99:
            break
        elif memory[pointer] == 1:
            memory[memory[pointer+3]] = memory[memory[pointer+1]] + memory[memory[pointer+2]]
        elif memory[pointer] == 2:
            memory[memory[pointer+3]] = memory[memory[pointer+1]] * memory[memory[pointer+2]]
        pointer += 4
    return memory[0]

def pt2(input):
    program = [int(x) for x in input[0].split(",")]

    for n in range(100):
        for v in range(100):
            memory = program.copy()
            memory[1] = n
            memory[2] = v

            pointer = 0
            while True:
                if memory[pointer] == 99:
                    break
                elif memory[pointer] == 1:
                    memory[memory[pointer+3]] = memory[memory[pointer+1]] + memory[memory[pointer+2]]
                elif memory[pointer] == 2:
                    memory[memory[pointer+3]] = memory[memory[pointer+1]] * memory[memory[pointer+2]]
                pointer += 4
            if memory[0] == 19690720:
                return (n, v)

if __name__ == "__main__":
    import cProfile

    input = open("../input/02", "r").readlines()
    cProfile.run("pt1(input)")
    cProfile.run("pt2(input)")
    print(pt1(input))
    print(pt2(input))
