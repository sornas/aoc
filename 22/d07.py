import sys

def main():
    lines = [s.strip() for s in sys.stdin.readlines()]
    l = 0
    cwd = "/"
    dirs = {}
    subdirs = {}
    while l < len(lines):
        line = lines[l]
        if line[0] == "$":
            # cmd
            cmd = line.split(" ")[1]
            if cmd == "cd":
                arg = line.split(" ")[2]
                if arg == "/":
                    cwd = "/"
                elif arg == "..":
                    cwd = "/".join(cwd.split("/")[:-2]) + "/"
                else:
                    cwd += arg + "/"
                if cwd not in dirs:
                    dirs[cwd] = []
                    subdirs[cwd] = []
                l += 1
            elif cmd == "ls":
                l += 1
                while l < len(lines) and not lines[l].startswith("$"):
                    if lines[l].startswith("dir"):
                        subdirs[cwd].append(lines[l].split(" ")[1])
                        l += 1
                        continue
                    size, fname = lines[l].split()
                    dirs[cwd].append((fname, int(size)))
                    l += 1
    print(dirs)
    print(subdirs)

    def sizeof(d):
        return sum(size for _, size in dirs[d]) + sum(sizeof(d + sd + "/") for sd in subdirs[d])

    dir_sizes = [sizeof(d) for d in dirs]
    print(sum(s for s in dir_sizes if s < 100000))

    tot = 70000000
    want = 30000000
    used = sizeof("/")
    unused = tot - used
    need = want - unused
    print(list(sorted(s for s in dir_sizes if s > need))[0])


main()
