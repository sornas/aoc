import collections
import intcode
import sys

program = [int(x) for x in open("../input/23", "r").readline().split(",")]

computers = [intcode.Computer(program, network_id=i) for i in range(50)]
queues = [collections.deque([i]) for i in range(len(computers))]
output_buffers = [[] for _ in range(len(computers))]
waiting = [False for _ in range(len(computers))]

prev_nat_x, prev_nat_y = -1, -1
nat_x, nat_y = 0, 0

while True:
    for i in range(len(computers)):
        c = computers[i]
        c.step()
        if c.SIG_INPUT:
            if len(queues[i]) > 0:
                c.input = queues[i].popleft()
                waiting[i] = False
            else:
                c.input = -1
                waiting[i] = True
        if c.SIG_OUTPUT:
            output_buffers[i].append(c.output)
            c.output = None
            waiting[i] = False
            if len(output_buffers[i]) == 3:
                addr, x, y = output_buffers[i]
                output_buffers[i] = []
                if addr == 255:
                    nat_x, nat_y = x, y
                else:
                    queues[addr].append(x)
                    queues[addr].append(y)
    empty_queues = True
    for q in queues:
        if len(q) > 0:
            empty_queues = False
            break
    all_waiting = True
    for w in waiting:
        if not w:
            all_waiting = False
            break
    if empty_queues and all_waiting:
        queues[0].append(nat_x)
        queues[0].append(nat_y)
        if nat_y == prev_nat_y:
            print(nat_y)
            sys.exit()
        prev_nat_x, prev_nat_y = nat_x, nat_y
