#!/usr/bin/env python3
import aoc20
import sys


def pt1(_in):
    nums = [int(n) for n in _in]
    for i, n1 in enumerate(nums):
        for n2 in nums[i:]:
            if n1 + n2 == 2020:
                return n1 * n2


def pt2(_in):
    nums = [int(n) for n in _in]
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums[i:]):
            if n1 + n2 > 2020:
                continue
            for n3 in nums[i+j:]:
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 1)
    print(pt1(input))
    print(pt2(input))
