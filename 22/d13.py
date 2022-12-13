import sys

def main():
    def cmp(l, r):
        print(l, r)
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


    s = 0
    for p, packet in enumerate(sys.stdin.read().split("\n\n")):
        left, right = list(map(eval, packet.strip().split("\n")))
        res = cmp(left, right)
        print(p, left, right, res)
        print()
        if res[0]:
            s += p + 1
    print(s)

main()
