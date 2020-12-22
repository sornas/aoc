import aoc20
import sys
from collections import deque
import functools
import itertools


def pt1(_in):
    _in = "".join(_in)
    player1 = deque([int(n) for n in _in.split("\n\n")[0].split("\n")[1:]])
    player2 = deque([int(n) for n in _in.split("\n\n")[1].split("\n")[1:-1]])

    while all((player1, player2)):
        c1, c2 = player1.popleft(), player2.popleft()
        if c1 > c2:
            player1.append(c1)
            player1.append(c2)
        else:
            player2.append(c2)
            player2.append(c1)

    return sum((i+1) * v
               for i, v in enumerate(reversed(player1 if player1 else player2)))


mem = dict()
def play(player1, player2):
    call_state = tuple((tuple(player1), tuple(player2)))
    if call_state in mem:
        return mem[call_state]
    seen = set()
    while all((player1, player2)):
        state = tuple((tuple(player1), tuple(player2)))
        if state in seen:
            mem[call_state] = 1
            return 1
        seen.add(state)
        c1, c2 = player1.popleft(), player2.popleft()
        if all(len(p) >= c for c, p in zip((c1,c2), (player1, player2))):
            win = play(deque(itertools.islice(player1, 0, c1)), deque(itertools.islice(player2, 0, c2)))
        else:
            win = 1 if c1 > c2 else 2
        if win == 1:
            player1.append(c1)
            player1.append(c2)
        else:
            player2.append(c2)
            player2.append(c1)
    mem[call_state] = 1 if player1 else 2
    return 1 if player1 else 2



def pt2(_in):
    _in = "".join(_in)
    player1 = deque([int(n) for n in _in.split("\n\n")[0].split("\n")[1:]])
    player2 = deque([int(n) for n in _in.split("\n\n")[1].split("\n")[1:-1]])
    play(player1, player2)
    return sum((i+1) * v
               for i, v in enumerate(reversed(player1 if player1 else player2)))

if __name__ == "__main__":
    _in = aoc20.read_input(sys.argv[1:], 22)
    print(pt1(_in))
    print(pt2(_in))
