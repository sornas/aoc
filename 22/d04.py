import sys

def main():
    c1 = 0
    c2 = 0
    for pairs in sys.stdin.readlines():
        first, second = pairs.strip().split(",")
        f1, f2 = list(map(int, first.split("-")))
        s1, s2 = list(map(int, second.split("-")))
        if (f1 >= s1 and f2 <= s2) or (s1 >= f1 and s2 <= f2):
            c1 += 1
        if ((f2 >= s1 and f1 <= s1) or (s2 >= f1 and s1 <= f1)):
            c2 += 1
    print(c1)
    print(c2)

main()
