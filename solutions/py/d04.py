from collections import Counter

def isIncreasing(num):
    s = list(str(num))
    n = int(s[0])
    n_i = 0
    for sp in s[1:]:
        n_i += 1
        if int(sp) < n:
            for i in range(n_i, 6):
                s[i] = str(n)
            return False, int("".join(s))
        n = int(sp)
    return (True,)

def pt1(input):
    def containsDouble(num):
        s = str(num)
        amounts = [0 for _ in range(10)]
        for c in s:
            amounts[int(c)] += 1
        c = Counter(amounts)
        return c[0] + c[1] < 10

    amount = 0
    n = 357253
    while n < 892942 + 1:
        inc = isIncreasing(n)
        if inc[0] == True:
            if containsDouble(n):
                amount += 1
            n += 1
        else:
            n = inc[1]
    return amount

def pt2(input):
    def containsDouble(num):
        s = str(num)
        amounts = [0 for _ in range(10)]
        for c in s:
            amounts[int(c)] += 1
        c = Counter(amounts)
        if c[0] + c[1] < 10:
            return c[2] >= 1

    amount = 0
    n = 357253
    while n < 892942 + 1:
        inc = isIncreasing(n)
        if inc[0] == True:
            if containsDouble(n):
                amount += 1
            n += 1
        else:
            n = inc[1]
    return amount

if __name__ == "__main__":
    import cProfile

    cProfile.run("pt1([])")
    cProfile.run("pt2([])")
    print(pt1([]))
    print(pt2([]))
