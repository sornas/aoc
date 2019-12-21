import time

import d01
import d02
import d03
import d04
import d05
import d06
import d07
import d08
import d09
import d10
import d11
import d12
import d13
import d14
import d15
import d16
import d17
import d18
import d19
import d20
import d21

mods = [d01, d02, d03, d04, d05, d06, d07, d08, d09, d10, \
        d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, \
        d21]

skip = []

for mod, day in zip(mods, range(len(mods))):
    if day+1 == 18:
        print("input changed between part 1 and part 2, run it separatly")
        continue
    elif day+1 in skip:
        continue
    print("Day", str(day+1).zfill(2))
    print("Part", 1, mod.pt1(open("../input/" + str(day+1).zfill(2), "r").readlines()))
    print("Part", 2, mod.pt2(open("../input/" + str(day+1).zfill(2), "r").readlines()))
