#!/usr/bin/env python3
import aoc20
import sys


def pt1(_in):
    nums = [int(n) for n in _in[0].split(",")]
    prev = {n: i for i, n in enumerate(nums)}
    while len(nums) < 2020:
        cur = nums[-1]
        if cur not in prev:
            nums.append(0)
            prev[cur] = len(nums) - 2
        else:
            nums.append(len(nums) - 1 - prev[cur])
            prev[cur] = len(nums) - 2
    return nums[2019]


def pt2(_in):
    nums = [int(n) for n in _in[0].split(",")]
    amount = 3
    cur = nums[-1]
    prev = {n: i for i, n in enumerate(nums)}
    while amount < 30000000:
        if amount % 300000 == 0:
            print(amount // 300000)
        if cur not in prev:
            new = 0
            prev[cur] = amount - 1
        else:
            new = amount - 1 - prev[cur]
            prev[cur] = amount - 1
        cur = new
        amount += 1
    return cur


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 15)
    print(pt1(input))
    print(pt2(input))
