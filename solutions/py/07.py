import itertools
import queue
import sys

params = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0}
ADD = 1
MULT = 2
IN = 3
OUT = 4
JNZ = 5
JEZ = 6
LET = 7
EQV = 8
HAL = 99

class Computer(object):
    def __init__(self, program):
        self.memory = program.copy()
        self.pointer = 0
        self.phase_read = False

        self.input = None
        self.output = None

    def parse_op(self, op):
        code = op % 100
        return [code] + [(op // 10**(i+2)) % 10**(i+1) for i in range(params[code])]

    def clear_flags(self):
        self.input  = None
        self.output = None

    def get_param(self, inst, num):
        return self.memory[self.pointer + num] if inst[num] == True else\
                self.memory[self.memory[self.pointer + num]]

    def step(self):
        inst = self.parse_op(self.memory[self.pointer])
        if inst[0] == HAL:
            return
        elif inst[0] == ADD:
            self.memory[self.memory[self.pointer+3]] = \
                    self.get_param(inst, 1) + self.get_param(inst, 2)
            self.pointer += 4
        elif inst[0] == MULT:
            self.memory[self.memory[self.pointer+3]] = \
                    self.get_param(inst, 1) * self.get_param(inst, 2)
            self.pointer += 4
        elif inst[0] == IN:
            self.memory[self.memory[self.pointer+1]] = self.input
            self.input = None
            self.pointer += 2
        elif inst[0] == OUT:
            self.output = self.get_param(inst, 1)
            self.pointer += 2
        elif inst[0] == JNZ:
            if self.get_param(inst, 1) != 0:
                self.pointer = self.get_param(inst, 2)
            else:
                self.pointer += 3
        elif inst[0] == JEZ:
            if self.get_param(inst, 1) == 0:
                self.pointer = self.get_param(inst, 2)
            else:
                self.pointer += 3
        elif inst[0] == LET:
            self.memory[self.memory[self.pointer+3]] = 1 if \
                    self.get_param(inst, 1) < self.get_param(inst, 2) \
                    else 0
            self.pointer += 4
        elif inst[0] == EQV:
            self.memory[self.memory[self.pointer+3]] = 1 if \
                    self.get_param(inst, 1) == self.get_param(inst, 2) \
                    else 0
            self.pointer += 4
        else:
            print(self.memory)
            print(self.pointer)
            print("invalid instruction", self.memory[self.pointer])
            print(inst)
            sys.exit()

def pt2(program):
    highest_signal = 0
    highest_sequence = None
    for phase_seq in list(itertools.permutations(list(range(5,10)))):
        signal = 0
        q = queue.Queue(5)
        for phase in phase_seq:
            q.put(phase)
        amps = [Computer(program) for i in range(5)]
        for amp in amps:
            amp.input = q.get()

        signal = 0
        current_amp = 0
        while True:
            amp = amps[current_amp]
            amp.step()
            if amp.input == None:
                if amp.phase_read == False:
                    amp.phase_read = True
                    amp.input = signal
                else:
                    pass
            if amp.output is not None:
                signal = amp.output
                amp.output = None
                current_amp = (current_amp + 1) % 5
                if amps[current_amp].phase_read == True:
                    amps[current_amp].input = signal
                continue
            if amp.memory[amp.pointer] == 99:
                if current_amp == 4:
                    break
                current_amp = (current_amp + 1) % 5
                amps[current_amp].input = signal
                continue
        if signal > highest_signal:
            highest_signal = signal
            highest_sequence = phase_seq
    return highest_signal

if __name__ == "__main__":
    f = open("../input/07", "r")
    program = [int(x) for x in f.readline().split(",")]

    import cProfile
    import timeit

    print(pt2(program))
    print(timeit.timeit('pt2(program)', globals=globals(), number=1)*1000, "ms")
    cProfile.run("pt2(program)")
