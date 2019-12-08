import intcode
import itertools
import queue

def pt1(input):
    program = [int(x) for x in input[0].split(",")]
    highest_signal = 0
    highest_sequence = None
    for phase_seq in list(itertools.permutations(list(range(0,5)))):
        q = queue.Queue(5)
        for phase in phase_seq:
            q.put(phase)
        amps = [intcode.Computer(program) for _ in range(5)]
        for amp in amps:
            amp.input = q.get()
        signal = 0
        for amp in amps:
            while True:
                amp.step()
                if amp.input is None:
                    amp.input = signal
                if amp.output is not None:
                    signal = amp.output
                    amp.output = None
                    break
        if signal > highest_signal:
            highest_signal = signal
            highest_sequence = phase_seq
    return (highest_sequence, highest_signal)

def pt2(input):
    program = [int(x) for x in input[0].split(",")]
    highest_signal = 0
    highest_sequence = None
    for phase_seq in list(itertools.permutations(list(range(5,10)))):
        q = queue.Queue(5)
        for phase in phase_seq:
            q.put(phase)
        amps = [intcode.Computer(program) for _ in range(5)]
        for amp in amps:
            amp.input = q.get()

        signal = 0
        current_amp = 0
        while True:
            amp = amps[current_amp]
            amp.step()
            if amp.input is None:
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
    return (highest_sequence, highest_signal)
