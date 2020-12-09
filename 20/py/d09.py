#!/usr/bin/env python3
import sys
from collections import deque


def intify(_in):
    return list(int(n.strip()) for n in _in)


def first_invalid(nums):
    valid = []
    for i in range(25):
        for j in range(i+1, 25):
            valid.append(nums[i] + nums[j])
    for i in range(25, len(nums)):
        if nums[i] not in valid:
            return nums[i]
        valid = valid[24:]
        offset = 0
        for j in range(1, 25)[::-1]:
            valid.insert(offset, nums[i - j] + nums[i])
            offset += j


def pt1(_in):
    return first_invalid(intify(_in))


def pt2(_in):
    _in = intify(_in)
    invalid = first_invalid(_in)

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
    print(pt1(input))
    print(pt2(input))
