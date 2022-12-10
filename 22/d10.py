import sys

def main():
    strength = 1
    ans = 0
    step = 0
    
    def maybe_inc():
        nonlocal strength, ans, step
        if (step + 20) % 40 == 0:
            print("increasing")
            ans += step * strength


    for inst in sys.stdin.readlines():
        if "addx" in inst:
            step += 1
            maybe_inc()
            step += 1
            maybe_inc()
            to_add = int(inst.strip().split(" ")[1])
            strength += to_add
            print(step, to_add, strength)
        else:
            step += 1
            maybe_inc()
        if step >= 220:
            break
    print(ans)


main()
