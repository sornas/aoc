import sys
import time

program = [int(x) for x in input().split(" ")]

start = time.time()

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
        # print(n, v, memory[0])
        if memory[0] == 19690720:
            print(n, v)
            print("took " + str(time.time() - start))
            sys.exit()

