from collections import Counter

def containsDouble(num):
    s = str(num)
    amounts = []
    for n in (0,1,2,3,4,5,6,7,8,9):
        amounts.append(s.count(str(n)))
    c = Counter(amounts)
    if c[0] + c[1] < 10:
        return c[2] >= 1

def isIncreasing(num):
    s = str(num)
    n = int(s[0])
    for sp in s[1:]:
        if int(sp) < n:
            return False
        n = int(sp)
    return True

if __name__ == "__main__":
    amount = 0
    for n in range(357253, 892942 + 1):
        if containsDouble(n):
            if isIncreasing(n):
                print(n)
                amount += 1
        if n % 10000 == 0:
            pass
            # print(n)
    print(amount)
