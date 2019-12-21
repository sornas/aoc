from collections import deque
param_amount = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1, 99:0}

ADD = 1
MUL = 2
IN = 3
OUT = 4
JNZ = 5
JEZ = 6
LET = 7
EQV = 8
BAS = 9
HAL = 99

class Computer(object):
    def __init__(self, program, ascii=False):
        self.program = program
        self.memory_size = len(self.program)
        self.instruction_cache = {}
        if ascii:
            self.SIG_ASCII = True

        self.reset()

    def reset(self):
        self.memory = self.program.copy()
        self.extra_memory = {}
        self.pointer = 0
        self.phase_read = False  # for day 7
        self.relative_base = 0

        self.input = None
        self.input_queue = deque()
        self.output = None

        self.SIG_INPUT = False
        self.SIG_OUTPUT = False
        self.SIG_HALT = False

    def parse_op(self, op):
        if op in self.instruction_cache:
            return self.instruction_cache[op]
        code = op % 100
        ops = str(op).zfill(param_amount[code]+2)
        self.instruction_cache[op] = [code] + [int(x) for x in ops[:-2][::-1]]
        return self.instruction_cache[op]

    def write(self, addr, val):
        if addr >= self.memory_size:
            self.extra_memory[addr] = val
        else:
            self.memory[addr] = val

    def get(self, addr):
        if addr >= self.memory_size:
            return self.extra_memory.get(addr, 0)
        return self.memory[addr]

    def get_param(self, inst, num):
        if inst[num] == 0:
            return self.get(self.get(self.pointer + num))
        elif inst[num] == 1:
            return self.get(self.pointer + num)
        elif inst[num] == 2:
            return self.get(self.relative_base + self.get(self.pointer + num))

    def write_param(self, inst, num, val):
        if inst[num] == 0:
            self.write(self.get(self.pointer + num), val)
        elif inst[num] == 1:
            self.write(self.pointer + num, val)
        elif inst[num] == 2:
            self.write(self.relative_base + self.get(self.pointer + num), val)

    def queue_input(self, data: list):
        for val in data:
            self.input_queue.append(data)

    def queue_ascii(self, data: str, newline=True):
        for c in data:
            if c == "\n":
                self.input_queue.append(10)
            else:
                self.input_queue.append(ord(c))
        if newline:
            self.input_queue.append(10)

    def step(self):
        if self.SIG_OUTPUT and self.output is None:
            self.SIG_OUTPUT = False
        if self.SIG_INPUT and self.input is not None:
            self.SIG_INPUT = False

        inst = self.parse_op(self.memory[self.pointer])
        if inst[0] == HAL:
            self.SIG_HALT = True
            return
        elif inst[0] == ADD:
            self.write_param(inst, 3, \
                    self.get_param(inst, 1) + self.get_param(inst, 2))
            self.pointer += 4
        elif inst[0] == MUL:
            self.write_param(inst, 3, \
                    self.get_param(inst, 1) * self.get_param(inst, 2))
            self.pointer += 4
        elif inst[0] == IN:
            if self.SIG_ASCII and len(self.input_queue) != 0:
                self.input = self.input_queue.popleft()
            if self.input is None:
                self.SIG_INPUT = True
                return
            self.write_param(inst, 1, self.input)
            self.input = None
            self.SIG_INPUT = False
            self.pointer += 2
        elif inst[0] == OUT:
            if self.SIG_OUTPUT:
                return
            self.output = self.get_param(inst, 1)
            self.SIG_OUTPUT = True
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
            self.write_param(inst, 3, 1 if \
                    self.get_param(inst, 1) < self.get_param(inst, 2) \
                    else 0)
            self.pointer += 4
        elif inst[0] == EQV:
            self.write_param(inst, 3, 1 if \
                    self.get_param(inst, 1) == self.get_param(inst, 2) \
                    else 0)
            self.pointer += 4
        elif inst[0] == BAS:
            self.relative_base += self.get_param(inst, 1)
            self.pointer += 2
        else:
            print(self.memory)
            print(self.pointer)
            print("invalid instruction", self.memory[self.pointer])
            print(inst)
