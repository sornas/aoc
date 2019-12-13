import itertools
import primefac

class Moon(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dx = 0
        self.dy = 0
        self.dz = 0

    def step(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    def gx(self, other):
        if self.x < other.x:
            self.dx += 1
            other.dx -= 1

    def gy(self, other):
        if self.y < other.y:
            self.dy += 1
            other.dy -= 1

    def gz(self, other):
        if self.z < other.z:
            self.dz += 1
            other.dz -= 1

    def gravity(self, other):
        self.gx(other)
        self.gy(other)
        self.gz(other)

    def get_x(self):
        return self.x, self.dx

    def get_y(self):
        return self.y, self.dy

    def get_z(self):
        return self.z, self.dz

    def get(self):
        return self.get_x, self.get_y, self.get_z

def pt1(input):
    moons = []

    for line in input:
        dims = line.rstrip().split(",")
        x = int(dims[0][3:])
        y = int(dims[1][3:])
        z = int(dims[2][3:-1])
        moons.append(Moon(x, y, z))

    for _ in range(1000):
        for pair in itertools.permutations(moons, 2):
            pair[0].gravity(pair[1])
        for moon in moons:
            moon.step()

    tot = 0
    for moon in moons:
        pot = abs(moon.x) + abs(moon.y) + abs(moon.z)
        kin = abs(moon.dx) + abs(moon.dy) + abs(moon.dz)
        tot += pot*kin
    return tot

def get_cycle(init_pos, init_vel):
    initial = tuple(init_pos)
    pos = init_pos.copy()
    vel = init_vel.copy()
    iters = 0
    while 1:
        for i, j in itertools.permutations(range(4), 2):
            if i == j:
                continue
            if pos[i] < pos[j]:
                vel[i] += 1
                vel[j] -= 1
        for i in range(4):
            pos[i] += vel[i]
        iters += 1
        if pos[0] == initial[0] and pos[1] == initial[1] and \
                pos[2] == initial[2] and pos[3] == initial[3] and \
                vel[0] == 0 and vel[1] == 0 and \
                vel[2] == 0 and vel[3] == 0:
            return iters

def pt2(input):
    moons = []
    xs = 0
    ys = 0
    zs = 0

    for line in input:
        dims = line.rstrip().split(",")
        x = int(dims[0][3:])
        y = int(dims[1][3:])
        z = int(dims[2][3:-1])
        moons.append(Moon(x, y, z))

    xs = get_cycle([moon.x for moon in moons], [0 for _ in range(4)])
    ys = get_cycle([moon.y for moon in moons], [0 for _ in range(4)])
    zs = get_cycle([moon.z for moon in moons], [0 for _ in range(4)])

    factors = [primefac.factorint(n) for n in (xs, ys, zs)]
    nums = {}
    for factor in factors:
        for n in factor:
            nums[n] = max(nums.get(n, 0), factor[n])
    ans = 1
    for n in nums:
        ans *= n ** nums[n]
    return ans

if __name__ == "__main__":
    input = open("../input/12", "r").readlines()
    print(pt1(input))
    print(pt2(input))
