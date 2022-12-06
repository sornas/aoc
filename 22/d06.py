import sys

def main():
    line = sys.stdin.read()
    d1 = None
    d2 = None
    for i in range(3, len(line)):
        if d1 and d2:
            break
        if not d1 and len(set(line[i:i+4])) == 4:
            d1 = i+4
        if len(set(line[i:i+14])) == 14:
            d2=i+14
    print(f"Part 1: {d1}")
    print(f"Part 2: {d2}")

main()
