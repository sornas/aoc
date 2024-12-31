import aoc20
import sys

def pt1(inp):
    cups = list(map(int, inp[0].strip()))
    m = max(cups)

    # i = 0
    # for _ in range(100):
    #     cur = cups[i]
    #     v1 = cups[(i + 1) % len(cups)]
    #     v2 = cups[(i + 2) % len(cups)]
    #     v3 = cups[(i + 3) % len(cups)]
    #     cups.remove(v1)
    #     cups.remove(v2)
    #     cups.remove(v3)
    #     dst = cur - 1
    #     if dst == 0:
    #         dst += m
    #     while dst in (v1, v2, v3):
    #         dst -= 1
    #         if dst == 0:
    #             dst += m
    #     dst_idx = cups.index(dst)
    #     cups.insert(dst_idx + 1, v3)
    #     cups.insert(dst_idx + 1, v2)
    #     cups.insert(dst_idx + 1, v1)
    #     i = (i + 1) % len(cups)
    ...


def pt2(inp):
    cups = list(map(int, inp[0].strip()))
    # m = max(cups)
    cups += list(range(max(cups) + 1, 1000000 + 1))
    m = 1000000

    nxt = [None for _ in range(m+1)]
    for a, b in zip(cups, cups[1:]):
        nxt[a] = b
    nxt[b] = cups[0]

    curr = cups[0]
    for i in range(10000000):
        if i % 100000 == 0:
            print(i // 100000)
        pick = [nxt[curr], nxt[nxt[curr]], nxt[nxt[nxt[curr]]]]
        nxt[curr] = nxt[pick[2]]
        dst = curr - 1
        if dst == 0:
            dst = m
        while dst in pick:
            dst -= 1
            if dst == 0:
                dst = m
        
        # patch in
        nxt[pick[2]] = nxt[dst]
        nxt[dst] = pick[0]

        curr = nxt[curr]

    return nxt[1] * nxt[nxt[1]]


if __name__ == "__main__":
    _in = aoc20.read_input(sys.argv[1:], 22)
    print(pt1(_in))
    print(pt2(_in))
