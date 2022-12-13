import heapq
import sys

def main():
    m = {}
    for y, line in enumerate(sys.stdin.readlines()):
        for x, h in enumerate(line):
            if h == "S":
                start = (x, y)
                m[(x, y)] = ord('a')
            elif h == "E":
                goal = (x, y)
                m[(x, y)] = ord('z')
            else:
                m[(x, y)] = ord(h)

    print(m)

    def ns(x, y):
        res = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            p = (x+dx, y+dy)
            if p in m:
                res.append(p)
        return res

    seen = set()
    paths = [(0, goal)]

    while True:
        l, cur = heapq.heappop(paths)
        if cur in seen:
            continue
        seen.add(cur)
        if m[cur] == ord('a'):
            print(l)
            break
        for n in ns(*cur):
            if m[n] >= m[cur] - 1 and n not in seen: # <= <= ?
                heapq.heappush(paths, (l + 1, n))

main()
