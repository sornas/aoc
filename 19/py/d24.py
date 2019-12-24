class hashdict(dict):
    """
    hashable dict implementation, suitable for use as a key into
    other dicts.

        >>> h1 = hashdict({"apples": 1, "bananas":2})
        >>> h2 = hashdict({"bananas": 3, "mangoes": 5})
        >>> h1+h2
        hashdict(apples=1, bananas=3, mangoes=5)
        >>> d1 = {}
        >>> d1[h1] = "salad"
        >>> d1[h1]
        'salad'
        >>> d1[h2]
        Traceback (most recent call last):
        ...
        KeyError: hashdict(bananas=3, mangoes=5)

    based on answers from
       http://stackoverflow.com/questions/1151658/python-hashable-dicts

    """
    def __key(self):
        return tuple(sorted(self.items()))
    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__,
            ", ".join("{0}={1}".format(
                    str(i[0]),repr(i[1])) for i in self.__key()))

    def __hash__(self):
        return hash(self.__key())
    def __setitem__(self, key, value):
        raise TypeError("{0} does not support item assignment"
                         .format(self.__class__.__name__))
    def __delitem__(self, key):
        raise TypeError("{0} does not support item assignment"
                         .format(self.__class__.__name__))
    def clear(self):
        raise TypeError("{0} does not support item assignment"
                         .format(self.__class__.__name__))
    def pop(self, *args, **kwargs):
        raise TypeError("{0} does not support item assignment"
                         .format(self.__class__.__name__))
    def popitem(self, *args, **kwargs):
        raise TypeError("{0} does not support item assignment"
                         .format(self.__class__.__name__))
    def setdefault(self, *args, **kwargs):
        raise TypeError("{0} does not support item assignment"
                         .format(self.__class__.__name__))
    def update(self, *args, **kwargs):
        raise TypeError("{0} does not support item assignment"
                         .format(self.__class__.__name__))
    # update is not ok because it mutates the object
    # __add__ is ok because it creates a new object
    # while the new object is under construction, it's ok to mutate it
    def __add__(self, right):
        result = hashdict(self)
        dict.update(result, right)
        return result

def inside(p):
    return 0 <= p[0] < 5 and 0 <= p[1] < 5

def neighbours(p):
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), \
            (p[0], p[1]+1), (p[0], p[1]-1)]

def draw(bugs):
    s = ""
    for y in range(5):
        s += "\n"
        for x in range(5):
            if bugs[(x,y)] == True:
                s += "#"
            else:
                s += "."
    return s

def draw_nums(bugs):
    s = ""
    for y in range(5):
        s += "\n"
        for x in range(5):
            s += str(bugs.get((x,y), 0))
    return s

def nums(bugs):
    nums = {}
    for y in range(5):
        for x in range(5):
            p = (x,y)
            if bugs[p] == True:
                for n in neighbours(p):
                    if inside(n):
                        nums[n] = nums.get(n, 0) + 1
    return nums

f = open("../input/24", "r").readlines()

bugs = {}
for y in range(5):
    for x in range(5):
        bugs[(x,y)] = (f[y][x] == "#")

seen = set()
while True:
    h = hashdict(bugs.copy())
    if h in seen:
        break
    seen.add(h)
    new = {}
    ns = nums(bugs)
    for y in range(5):
        for x in range(5):
            p = (x,y)
            n = ns.get(p, 0)
            if bugs[p] == False and (n == 1 or n == 2):
                new[p] = True
            elif bugs[p] == True and n != 1:
                new[p] = False
            else:
                new[p] = bugs[p]
    bugs = new
print(draw(bugs))

ans = 0
for k, v in bugs.items():
    if v == True:
        ans += 2**(k[1]*5 + k[0])
print(ans)
