#!/usr/bin/env python3
import sys
import time


def read_input(args, day):
    if len(args) > 0:
        if args[0] == "-":
            return sys.stdin.readlines()
        else:
            return open(args[0]).readlines()
    else:
        return open(f"../input/{day:02}", "r").readlines()


if __name__ == "__main__":
    import d01
    import d02
    import d03
    import d04
    import d05
    import d06
    import d07
    import d08
    import d09

    skip = set()
    only = set()
    only_part = 0
    run_times = 1
    input_root = "../input"

    argv, argc = sys.argv, len(sys.argv)
    i = 1
    while i < argc:
        if argv[i] == "--help":
            print(f"usage: {argv[0]} [--help] [--time [times]] [--skip <n> <n> ...]\n" +
                   "       [--only <n> <n> ...] [--part 0|1|2] [--input <dir>]")
            sys.exit(0)
        elif argv[i] == "--time":
            i += 1
            if i < argc and not argv[i].startswith("-"):
                run_times = int(argv[i])
                i += 1
            else:
                run_times = 10
        elif argv[i] == "--skip":
            i += 1
            while i < argc and not argv[i].startswith("-"):
                skip.add(int(argv[i]))
                i += 1
        elif argv[i] == "--only":
            i += 1
            while i < argc and not argv[i].startswith("-"):
                only.add(int(argv[i]))
                i += 1
        elif argv[i] == "--part":
            i += 1
            only_part = int(argv[i])
            i += 1
        elif argv[i] == "--input":
            i += 1
            input_root = argv[i]
            i += 1
        else:
            print(f"unknown argument {argv[i]}")
            print(f"maybe try {argv[0]} --help ?")
            i += 1

    def running_part(part):
        return only_part == 0 or part == only_part

    print("    ", end="")
    if running_part(1):
        print("  -------Part 1--------", end="")
    if running_part(2):
        print("   -------Part 2--------", end="")
    print()
    print("Day", end="")
    print("     Time            Ans  ", end="")
    if only_part == 0:
        print("   Time            Ans  ", end="")
    print(" Total time")

    tot_time, tot_time_part = 0, [0, 0]
    runs = 0
    for day, mod in enumerate((d01, d02, d03, d04, d05,
                               d06, d07, d08, d09)):
        if day+1 in skip or (only and day+1 not in only):
            continue
        input = open(f"{input_root}/{day+1:02}").readlines()
        print(f" {day+1:2}   ", end="")
        for part, part_func in enumerate((mod.pt1, mod.pt2)):
            if not running_part(part+1):
                continue
            times = []
            for i in range(run_times):
                start = time.time()
                ans = part_func(input)
                ans_time = time.time()
                times.append(ans_time-start)
            avg_time = sum(times) / len(times)
            tot_time += avg_time
            tot_time_part[part] += avg_time
            print(f"{avg_time*1000:6.3f} {ans:14}   ", end="")
        print(f"{tot_time*1000:8.3f}")

        runs += 1
    print("    ---------", end="")
    if only_part == 0:
        print("                ---------", end="")
    print()
    print("avg   ", end="")
    if only_part in (0, 1):
        print(f"{tot_time_part[0]*1000/runs:6.3f}", end="")
    if only_part == 0:
        print("                   ", end="")
    if only_part in (0, 2):
        print(f"{tot_time_part[1]*1000/runs:6.3f}", end="")
    print()
