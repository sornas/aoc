import functools
import math
import sys

def main():
    def cmp(l, r):
        if type(l) is int:
            return cmp([l], r)
        if type(r) is int:
            return cmp(l, [r])
        if not l:
            return True, False
        if not r:
            return False, False
        if type(l[0]) is list or type(r[0]) is list:
            c, eq = cmp(l[0], r[0])
        else:
            c, eq = l[0] < r[0], l[0] == r[0]
        if c:
            return True, False
        if eq:
            return cmp(l[1:], r[1:])
        else:
            return False, False

    stdin = sys.stdin.read()
    s = 0
    for p, packet in enumerate(stdin.split("\n\n")):
        left, right = list(map(eval, packet.strip().split("\n")))
        res = cmp(left, right)
        if res[0]:
            s += p + 1
    print("1", s)

    lines = stdin.strip().split("\n")
    lines = [(l, False) for l in lines if l]
    lines += [("[[2]]", True), ("[[6]]", True)]
    def cmp_(l, r):
        c = cmp(eval(l[0]), eval(r[0]))
        if c[0]:
            return 1
        if c[1]:
            return 0
        return -1
    lines.sort(key=functools.cmp_to_key(lambda l, r: cmp_(l, r)))
    lines = list(enumerate(lines[::-1]))
    print("2", math.prod(l[0]+1 for l in lines if l[1][1]))

main()
