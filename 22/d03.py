import sys

def main():
    rucksacks = [l.strip() for l in sys.stdin.readlines()]
    s = 0
    for r in rucksacks:
        first = r[:-len(r)//2]
        second = r[len(r)//2:]
        common = list(set(first) & set(second))[0]
        if common.isupper():
            s += ord(common) - ord('A') + 27
        else:
            s += ord(common) - ord('a') + 1
    print(s)

    s = 0
    for i in range(0, len(rucksacks), 3):
        r1, r2, r3 = [rucksacks[i + j] for j in range(3)]
        common = list(set(r1) & set(r2) & set(r3))[0]
        if common.isupper():
            s += ord(common) - ord('A') + 27
        else:
            s += ord(common) - ord('a') + 1
    print(s)
main()
