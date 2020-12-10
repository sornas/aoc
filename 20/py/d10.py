#!/usr/bin/env python3
import aoc20
import functools
import sys


def pt1(_in):
    jolts = [int(n.strip()) for n in _in]
    jolts.append(max(jolts)+3)
    jolts = sorted(jolts)
    jolt = 0
    diffs = [0, 0, 0]
    for j in jolts:
        diffs[j-jolt-1] += 1
        jolt = j
    return diffs[0] * diffs[2]


def pt2(_in):
    jolts = [int(n.strip()) for n in _in]
    jolts.append(max(jolts)+3)
    jolts = sorted(jolts)
    jolts.insert(0, 0)
    jolt = 0
    reach = {}
    for i in range(len(jolts)):
        reachable = []
        j = i+1
        while j < len(jolts) and jolts[j] - jolts[i] <= 3:
            reachable.append(jolts[j])
            j += 1
        reach[jolts[i]] = tuple(reachable)

    @functools.cache
    def ways(start, dest):
        if start == dest:
            return 1
        return sum(ways(child, dest) for child in reach[start])

    return ways(jolts[0], jolts[-1])


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 10)
    print(pt1(input))
    print(pt2(input))
