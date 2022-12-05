import re
import sys

def main():
    lines = sys.stdin.read()
    piles = [[] for _ in range(10)]

    for line in lines.split("\n\n")[0].split("\n"):
        if not line.strip():
            break
        for i in range(10):
            if 4*i >= len(line):
                break
            if line[4*i] == "[":
                piles[i].insert(0, line[4*i + 1])

    piles1 = piles
    piles2 = [p.copy() for p in piles]

    for instruction in lines.split("\n\n")[1].split("\n"):
        match = re.search(r"move (\d+) from (\d) to (\d)", instruction)
        if not match:
            break
        amount, fr, to = list(map(int, match.groups()))
        for _ in range(amount):
            piles1[to-1].append(piles1[fr-1].pop())
        x = piles2[fr-1][-amount:]
        piles2[to-1] += x
        del piles2[fr-1][-amount:]
    for pile in piles1:
        if pile:
            print(pile[-1], end="")
    print()
    for pile in piles2:
        if pile:
            print(pile[-1], end="")
    print()

main()
