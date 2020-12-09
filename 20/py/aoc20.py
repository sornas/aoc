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


    print("day part | time   | tot_time | ans")
    print("---------+--------+----------+-----------")

    time_to_here = 0
    for day, mod in enumerate((d01, d02, d03, d04, d05,
                               d06, d07, d08, d09)):
        if day+1 in skip or (only and day+1 not in only):
            continue
        input = open(f"{input_root}/{day+1:02}").readlines()
        for part, part_func in enumerate((mod.pt1, mod.pt2)):
            if only_part != 0 and part+1 != only_part:
                continue
            times = []
            for i in range(run_times):
                start = time.time()
                ans = part_func(input)
                ans_time = time.time()
                times.append(ans_time-start)
            avg_time = sum(times) / len(times)
            time_to_here += avg_time
            print(f"{day+1:02}  {part+1}    | {avg_time*1000:6.3f} | {time_to_here*1000:6.3f}   | {ans}")
