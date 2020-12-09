#!/usr/bin/env python3
import aoc20
import sys


def pt1(_in):
    valid = 0
    want = {s for s in "byr iyr eyr hgt hcl ecl pid cid".split()}

    for line in _in:
        if line == "\n":
            if len(want) == 0 or (len(want) == 1 and "cid" in want):
                valid += 1
            want = {s for s in "byr iyr eyr hgt hcl ecl pid cid".split()}
            continue
        for entry in line.split(" "):
            want.remove(entry.split(":")[0])
    if len(want) == 0 or (len(want) == 1 and "cid" in want):
        valid += 1
    return valid


def valid_entry(k, v) -> bool:
    if k == "byr":
        try:
            v = int(v)
        except:
            return False
        return 1920 <= v <= 2002
    elif k == "iyr":
        try:
            v = int(v)
        except:
            return False
        return 2010 <= v <= 2020
    elif k == "eyr":
        try:
            v = int(v)
        except:
            return False
        return 2020 <= v <= 2030
    elif k == "hgt":
        cm = False
        try:
            if v[-2:] == "cm":
                cm = True
            elif v[-2:] != "in":
                return False
            v = int(v[:-2])
        except:
            return False
        if cm:
            return 150 <= v <= 193
        return 59 <= v <= 76
    elif k == "hcl":
        if v[0] != "#":
            return False
        if len(v) != 7:
            return False
        for c in v[1:]:
            if c not in "0123456789abcdef":
                return False
        return True
    elif k == "ecl":
        return v in "amb blu brn gry grn hzl oth".split()
    elif k == "pid":
        try:
            _ = int(v)
        except:
            return False
        return len(v) == 9
    elif k == "cid":
        return True


def pt2(_in):
    valid = 0
    want = {s for s in "byr iyr eyr hgt hcl ecl pid cid".split()}

    for line in _in:
        if line == "\n":
            if len(want) == 0 or (len(want) == 1 and "cid" in want):
                valid += 1
            want = {s for s in "byr iyr eyr hgt hcl ecl pid cid".split()}
            continue
        for entry in line.split(" "):
            k, v = entry.strip().split(":")
            if valid_entry(k, v):
                want.remove(k)
    if len(want) == 0 or (len(want) == 1 and "cid" in want):
        valid += 1
    return valid


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 4)
    print(pt1(input))
    print(pt2(input))
