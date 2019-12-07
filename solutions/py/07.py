import intcode
import itertools
import queue

def pt2(program):
    highest_signal = 0
    highest_sequence = None
    for phase_seq in list(itertools.permutations(list(range(5,10)))):
        signal = 0
        q = queue.Queue(5)
        for phase in phase_seq:
            q.put(phase)
        amps = [intcode.Computer(program) for i in range(5)]
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

    print(2, pt2(program))
    print(timeit.timeit('pt2(program)', globals=globals(), number=1)*1000, "ms")
    cProfile.run("pt2(program)")
