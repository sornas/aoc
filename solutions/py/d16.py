def do(input, phases=100, repeats=1):
    nums = []
    for i in range(repeats):
        nums += [int(x) for x in input[0].strip()]

    for phase in range(phases):
        print(phase)
        new_list = []
        for i in range(len(nums)):  # position of number to calculate
            new_num = 0
            for k in range(len(nums)):
                mod = (k+1) % (4*(i+1))
                if mod >= i + 1 and mod < 2*i + 2:
                    new_num += nums[k]
                elif mod >= 3*i + 3:
                    new_num -= nums[k]
            new_list.append(abs(new_num) % 10)
        nums = new_list
    return "".join([str(n) for n in nums[:8]])

def pt1(input):
    return do(input, phases=100, repeats=1)

def pt2(input, phases=100, repeats=10000):
    offset = int(input[0][:7])
    nums = []
    for i in range(repeats):
        nums += [int(x) for x in input[0].strip()]
    nums = nums[offset:]
    for phase in range(phases):
        print(phase)
        nums = nums[::-1]
        new_nums = []
        n = sum(nums)
        while len(nums) != 0:
            new_nums.append(abs(n) % 10)
            n -= nums.pop()
        nums = new_nums
    return "".join([str(n) for n in nums[:8]])

def square(size):
    s = ""
    for y in range(size):
        for x in range(size):
            mod = (x+1) % (4*(y+1))
            if mod < y+1:
                s += "0"
            elif mod < 2*y + 2:
                s += "+"
            elif mod < 3*y + 3:
                s += "0"
            else:
                s += "-"
            s += " "
        s += "\n"
    return s

if __name__ == "__main__":
    input = open("../input/16", "r").readlines()
    ans1 = pt1(input)
    ans2 = pt2(input)
    print(ans1)
    print(ans2)
    #print(square(8))
    #print(square(20))
    #print(square(62))
