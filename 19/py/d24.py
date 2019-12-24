import sys
class hashdict(dict):
    """
       http://stackoverflow.com/questions/1151658/python-hashable-dicts
    """
    def __key(self):
        return tuple(sorted(self.items()))
    def __hash__(self):
        return hash(self.__key())
    def __add__(self, right):
        result = hashdict(self)
        dict.update(result, right)
        return result

def inside(p):
    return 0 <= p[0] < 5 and 0 <= p[1] < 5

def neighbours(p):
    points = []
    for eql_n in [(p[0]+1, p[1]), (p[0]-1, p[1]), \
            (p[0], p[1]+1), (p[0], p[1]-1)]:
        if (eql_n[0], eql_n[1]) == (2,2):
            pf = (p[0], p[1])  # p flat (disregard dimension)
            if pf == (3,2):
                # right side of inner level (dim+1)
                points += [(4,y,p[2]+1) for y in range(5)]
            elif pf == (1,2):
                # left side of inner level
                points += [(0,y,p[2]+1) for y in range(5)]
            elif pf == (2,1):
                # upper side of inner level
                points += [(x,0,p[2]+1) for x in range(5)]
            elif pf == (2,3):
                # lower side of inner level
                points += [(x,4,p[2]+1) for x in range(5)]
        elif not inside(eql_n):
            if p[0] == 0:
                points.append((1,2,p[2]-1))
            elif p[0] == 4:
                points.append((3,2,p[2]-1))
            if p[1] == 0:
                points.append((2,1,p[2]-1))
            elif p[1] == 4:
                points.append((2,3,p[2]-1))
        else:
            points.append((eql_n[0], eql_n[1], p[2]))
    return list(set(points))

def draw_bugs(bugs, dim):
    s = ""
    for y in range(5):
        s += "\n"
        for x in range(5):
            if (x,y) == (2,2):
                s += "?"
            elif bugs[(x,y,dim)] == True:
                s += "#"
            else:
                s += "."
            s += " "
    return s

def draw_nums(nums,dim):
    s = ""
    for y in range(5):
        s += "\n"
        for x in range(5):
            if (x,y) == (2,2):
                s += "?"
            else:
                s += str(nums.get((x,y,dim), 0))
            s += " "
    return s

def draw_both(bugs, nums, dim):
    s = ""
    for y in range(5):
        s += "\n"
        for x in range(5):
            if (x,y) == (2,2):
                s += "??"
            else:
                s += ("#" if bugs[(x,y,dim)] == True else ".") + str(nums.get((x,y,dim), 0))
            s += " "
    return s

def nums(bugs, max_dims):
    nums = {}
    for dim in range(0-(max_dims+1), max_dims+2):
        for y in range(5):
            for x in range(5):
                p = (x,y,dim)
                if bugs.get(p, False) == True:
                    for n in neighbours(p):
                        nums[n] = nums.get(n, 0) + 1
    return nums

f = open("../input/24", "r").readlines()

bugs = {}
for y in range(5):
    for x in range(5):
        bugs[(x,y,0)] = (f[y][x] == "#")

seen = set()
for max_dim in range(200):
    new = {}
    #ns = nums(bugs, max_dim)
    num_bugs = 0
    for dim in range(0-(max_dim+1), max_dim+2):
        for y in range(5):
            for x in range(5):
                p = (x,y,dim)
                amount = 0
                for n in neighbours(p):
                    amount += 1 if bugs.get(n, False) == True else 0
                if bugs.get(p, False) == False and (amount == 1 or amount == 2):
                    new[p] = True
                elif bugs.get(p, False) == True and amount != 1:
                    new[p] = False
                else:
                    new[p] = bugs.get(p, False)
    bugs = new

bugs_per_dim = {}
for dim in range(0-(max_dim+1), max_dim+2):
    amount = 0
    for y in range(5):
        for x in range(5):
            if bugs[(x,y,dim)] == True:
                if (x,y) == (2,2):
                    continue
                amount += 1
    bugs_per_dim[dim] = amount
print(sum(bugs_per_dim.values()))
