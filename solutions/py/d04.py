from collections import Counter

def isIncreasing(num):
    s = str(num)
    n = int(s[0])
    for sp in s[1:]:
        if int(sp) < n:
            return False
        n = int(sp)
    return True

def pt1(input):
    def containsDouble(num):
        s = str(num)
        amounts = []
        for n in (0,1,2,3,4,5,6,7,8,9):  # herregud
            amounts.append(s.count(str(n)))
        c = Counter(amounts)
        return c[0] + c[1] < 10

    amount = 0
    for n in range(357253, 892942 + 1):
        if containsDouble(n):
            if isIncreasing(n):
                amount += 1
    return amount

def pt2(input):
    def containsDouble(num):
        s = str(num)
        amounts = []
        for n in (0,1,2,3,4,5,6,7,8,9):  # herregud
            amounts.append(s.count(str(n)))
        c = Counter(amounts)
        if c[0] + c[1] < 10:
            return c[2] >= 1
    amount = 0
    for n in range(357253, 892942 + 1):
        if containsDouble(n):
            if isIncreasing(n):
                amount += 1
    return amount

if __name__ == "__main__":
    import cProfile
    cProfile.run("pt1([])")
