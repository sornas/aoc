import collections
import functools
import heapq
import re
import sys

def main():
    tunnels = {}
    rate = {}
    for line in sys.stdin.read().strip().split("\n"):
        valve, rate_, to, *_ = re.match(
            r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? ((..(, )?)+)$",
            line
        ).groups()
        if rate_ != "0":
            rate[valve] = int(rate_)
        tunnels[valve] = to.split(", ")
    avail = frozenset(rate.keys())

    @functools.cache
    def path_between(fr, to):
        weights = {}
        new_batch = [(fr, 0)]
        while True:
            if not new_batch:
                return None
            batch = new_batch
            new_batch = []
            for p, l in batch:
                for n in tunnels[p]:
                    if n not in weights:
                        weights[n] = l + 1
                        new_batch.append((n, l + 1))
            if to in weights:
                return weights[to]

    hq = [(0, 0, "AA", frozenset())]
    seen = dict()
    best = 0
    furthest = 0
    while hq:
        steps, release, cur, opened = heapq.heappop(hq)
        if release > best:
            best = release
        if steps > furthest:
            print(steps)
            furthest = steps
        # opened_list = list(opened)
        # opened_list.sort()
        # opened_list = tuple(opened_list)
        # if (release, cur, opened_list) in seen:
        #     continue
        # seen.add((release, cur, opened_list))
        for other in avail - opened:
            # gå och öppna
            to_go = path_between(cur, other)
            if steps + to_go >= 30:
                # hinner inte
                continue
            heapq.heappush(hq, (
                steps + to_go + 1,
                release + (30 - (steps + to_go + 1)) * rate[other],
                other,
                opened | frozenset([other])
            ))
    print(best)

    # q = collections.deque([(0, 0, "AA", set())]) # (total_release, steps, cur, state, opened)
    # best = {}
    # while True:
    #     if q[0][1] == 30:
    #         break
    #     release, steps, cur, opened = q.popleft()
    #     state = (cur, frozenset(opened))
    #     if state in best and best[state] > release:
    #         continue
    #     best[state] = release
    #     print(steps, best)
    #     for tun in tunnels[cur]:
    #         q.append((release, steps + 1, tun, opened))
    #     if cur not in opened:
    #         # try opening
    #         q.append((release + (30 - steps - 1) * rate[cur], steps + 1, cur, opened | {cur}))
    #     # can also stay put
    #     q.append((release, steps + 1, cur, opened))
    # print(max(q))


main()
