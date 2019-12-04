import sys

program = [int(x) for x in input().split(",")]

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
print(memory[0])

