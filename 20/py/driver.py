#!/usr/bin/env python3
import sys
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


print("day part | time   | tot_time | ans")
print("---------+--------+----------+-----------")

time_to_here = 0
for day, mod in enumerate((d01, d02, d03, d04, d05,
                           d06, d07, d08, d09)):
    input = open(f"../input/{day+1:02}").readlines()
    for part, part_func in enumerate((mod.pt1, mod.pt2)):
        times = []
        for i in range(100 if "time" in sys.argv else 5):
            start = time.time()
            ans = part_func(input)
            ans_time = time.time()
            times.append(ans_time-start)
        avg_time = sum(times) / len(times)
        time_to_here += avg_time
        print(f"{day+1:02}  {part+1}    | {avg_time*1000:6.3f} | {time_to_here*1000:6.3f}   | {ans}")
