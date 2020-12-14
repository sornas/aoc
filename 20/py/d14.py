#!/usr/bin/env python3
import aoc20
import sys


def to_bin(n: int) -> str:
    return bin(n)[2:]  # 0b


def from_bin(b: str) -> int:
    return int(b, 2)


def mask(b: [str], m: [str]) -> [str]:
    # print(f"{b:>36}\n{m}")
    ret = ""
    for mi in range(len(m))[::-1]:
        bi = mi - (len(m) - len(b))
        if m[mi] == "0":
            ret = "0" + ret
        elif m[mi] == "1":
            ret = "1" + ret
        else:
            ret = (str(b[bi]) if bi >= 0 else "0") + ret
        # print(b, b[bi] if bi >= 0 else " ", m[mi], ret)
    # print(f"{ret:>36}")
    # print()
    return ret


def pt1(_in):
    mem = {}
    cur_mask = [-1 for _ in range(36)]
    for inst in _in:
        inst = inst.strip()
        if inst[:4] == "mask":
            cur_mask = inst.split(" = ")[1]
        else:
            key = int(inst[inst.index("[")+1:inst.index("]")])
            bits = to_bin(int(inst.split(" = ")[1]))
            bits = mask(bits, cur_mask)
            mem[key] = bits
    s = 0
    for k, v in mem.items():
        s += from_bin(v)
    return s


def str_set_at(s, c, i):
    return s[:i] + c + s[i+1:]


def mask2(b: [str], m: [str]) -> [[str]]:
    adr = ""
    for mi in range(len(m))[::-1]:
        bi = mi - (len(m) - len(b))
        if m[mi] == "0":
            adr = (str(b[bi]) if bi >= 0 else "0") + adr
        elif m[mi] == "1":
            adr = "1" + adr
        else:
            adr = "X" + adr
    adrs = [adr]
    for bit in range(len(adr)):
        if adr[bit] == "X":
            new_adrs = []
            while adrs:
                adr = adrs.pop()
                new_adrs.append(str_set_at(adr, "0", bit))
                new_adrs.append(str_set_at(adr, "1", bit))
            adrs = new_adrs
    return adrs


def pt2(_in):
    mem = {}
    cur_mask = [-1 for _ in range(36)]
    for inst in _in:
        inst = inst.strip()
        if inst[:4] == "mask":
            cur_mask = inst.split(" = ")[1]
        else:
            key = to_bin(int(inst[inst.index("[")+1:inst.index("]")]))
            keys = mask2(key, cur_mask)
            val = int(inst.split(" = ")[1])
            for key in keys:
                mem[key] = val
    return sum(mem.values())


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 14)
    print(pt1(input))
    print(pt2(input))
