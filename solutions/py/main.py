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

mods = [d01, d02, d03, d04, d05, d06, d07, d08, d09, d10]

timings = [[0 for _ in range(2)] for _ in range(len(mods))]
clock_type = time.CLOCK_MONOTONIC

for mod, day in zip(mods, range(len(mods))):
    print("Day", str(day+1).zfill(2))
    t0 = time.clock_gettime_ns(clock_type)
    print("Part", 1, mod.pt1(open("../input/" + str(day+1).zfill(2), "r").readlines()))
    timings[day][0] = time.clock_gettime_ns(clock_type) - t0
    t0 = time.clock_gettime_ns(clock_type)
    print("Part", 2, mod.pt2(open("../input/" + str(day+1).zfill(2), "r").readlines()))
    timings[day][1] = time.clock_gettime_ns(clock_type) - t0

print()
tot = 0
for day in range(len(timings)):
    for part in range(2):
        tot += timings[day][part]
for day in range(len(timings)):
    for part in range(2):
        print("day {0}-{1}: {2:.2f}ms\t({3:.1f}%)".format(str(day+1).zfill(2), part+1, \
            timings[day][part] / 1000000, 100*timings[day][part] / tot))
print("sum", tot / 1000000, "ms")
