#!/usr/bin/env python3
def pt1(_in):
    valid = 0
    for passwd in _in:
        want, have = passwd.split(":")
        want_num, want_char = want.split()
        want_min, want_max = [int(s) for s in want_num.split("-")]
        if want_min <= have.count(want_char) <= want_max:
            valid += 1
    return valid


def pt2(_in):
    valid = 0
    for passwd in _in:
        want, have = passwd.split(":")
        want_num, want_char = want.split()
        want_first, want_second = [int(s) for s in want_num.split("-")]
        matches = 0
        if have[want_first] == want_char:
            matches += 1
        if have[want_second] == want_char:
            matches += 1
        if matches == 1:
            valid += 1
    return valid


if __name__ == "__main__":
    input = open("../input/02", "r").readlines()
    print(pt1(input))
    print(pt2(input))
