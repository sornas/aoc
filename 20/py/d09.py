#!/usr/bin/env python3
import sys
from collections import deque


def intify(_in):
    return list(int(n.strip()) for n in _in)


def pt1(_in):
    valid = []
    for i in range(25):
        for j in range(i+1, 25):
            valid.append(_in[i] + _in[j])
    for i in range(25, len(_in)):
        if _in[i] not in valid:
            return _in[i]
        valid = valid[24:]
        offset = 0
        for j in range(1, 25)[::-1]:
            valid.insert(offset, _in[i - j] + _in[i])
            offset += j


def pt2(_in):
    invalid = pt1(_in)

    i, s, nums = 0, 0, deque()
    while s != invalid:
        if s < invalid:
            # add
            s += _in[i]
            nums.append(_in[i])
            i += 1
        else:
            # pop
            s -= nums[0]
            nums.popleft()
    return min(nums) + max(nums)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = open(sys.argv[1], "r").readlines()
    else:
        input = open("../input/09", "r").readlines()
    input = intify(input)
    print(pt1(input))
    print(pt2(input))
