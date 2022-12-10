import sys

def main():
    x = 1
    step = 0
    crt = [[] for _ in range(6)]

    def cycle():
        nonlocal x, step, crt
        crtx = step % 40
        crty = step // 40
        if x in range(crtx-1, crtx+2):
            crt[crty].append("#")
        else:
            crt[crty].append(".")
    
    for inst in sys.stdin.readlines():
        if "addx" in inst:
            cycle()
            step += 1
            cycle()
            step += 1
            to_add = int(inst.strip().split(" ")[1])
            x += to_add
        else:
            cycle()
            step += 1
        if step >= 240:
            break
    # print(ans)

    for y in range(6):
        for x in range(40):
            print(crt[y][x], end="")
        print()


main()
