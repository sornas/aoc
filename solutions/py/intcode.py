param_amount = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1, 99:0}

ADD = 1
MULT = 2
IN = 3
OUT = 4
JNZ = 5
JEZ = 6
LET = 7
EQV = 8
BAS = 9
HAL = 99

class Computer(object):
    def __init__(self, program):
        self.memory = program.copy()
        self.instruction_cache = {}
        self.pointer = 0
        self.phase_read = False  # for day 7
        self.relative_base = 0

        self.input = None
        self.output = None
        self.wants_input = False

    def parse_op(self, op):
        #TODO
        if op in self.instruction_cache:
            return self.instruction_cache[op]
        code = op % 100
        ops = str(op).zfill(param_amount[code]+2)
        self.instruction_cache[op] = [code] + [int(x) for x in ops[:-2][::-1]]
        return self.instruction_cache[op]
        #return [code] + [(op // 10**(i+2)) % 10**(i+1) for i in range(param_amount[code])]

    def clear_flags(self):
        self.input  = None
        self.output = None

    def write(self, addr, val):
        while addr >= len(self.memory):
            self.memory.append(0)
        self.memory[addr] = val

    def get(self, addr):
        while addr >= len(self.memory):
            self.memory.append(0)
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

    def step(self):
        inst = self.parse_op(self.memory[self.pointer])
        if inst[0] == HAL:
            return
        elif inst[0] == ADD:
            self.write_param(inst, 3, \
                    self.get_param(inst, 1) + self.get_param(inst, 2))
            self.pointer += 4
        elif inst[0] == MULT:
            self.write_param(inst, 3, \
                    self.get_param(inst, 1) * self.get_param(inst, 2))
            self.pointer += 4
        elif inst[0] == IN:
            if self.input is None:
                self.wants_input = True
                return
            self.write_param(inst, 1, self.input)
            self.wants_input = False
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
