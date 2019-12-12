import itertools
import math
f = open("../input/12", "r")

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

    def gravity(self, other):
        if self.x < other.x:
            self.dx += 1
            other.dx -= 1
        if self.y < other.y:
            self.dy += 1
            other.dy -= 1
        if self.z < other.z:
            self.dz += 1
            other.dz -= 1

    def get(self):
        return (self.x, self.y, self.z)

moons = []
for line in f.readlines():
    dims = line.rstrip().split(",")
    x = int(dims[0][3:])
    y = int(dims[1][3:])
    z = int(dims[2][3:-1])
    print(x,y,z)
    moons.append(Moon(x, y, z))

for moon, c in zip(moons, ["i", "e", "g", "c"]):
    moon.c = c

old_pos = {}

def draw(moons):
    min_x = min_y = min_z = max_x = max_y = max_z = 0
    pos = {}
    for moon in moons:
        min_x = min(min_x, moon.x)
        max_x = max(max_x, moon.x)
        min_y = min(min_y, moon.y)
        max_y = max(max_y, moon.y)
        min_z = min(min_z, moon.z)
        max_z = max(max_z, moon.z)
        pos[(moon.x, moon.y)] = moon.c

    for y in range(-20, 20):
        for x in range(-20, 20):
            b = False
            if (x,y) in pos:
                print(pos[(x,y)], end="")
                continue
            print(" ", end="")
        print()

# start
# i = 0
# while True:
#     if i % 70000 == 0:
#         print(i)
#     old_pos[(moon.get() for moon in moons)] = i
#     for pair in itertools.permutations(moons, 2):
#         pair[0].gravity(pair[1])
#     for moon in moons:
#         moon.step()
#     i += 1
#     if (moon.get() for moon in moons) in old_pos:
#         print("stop", i)
#         break
#
for i in range(1000):
    for pair in itertools.permutations(moons, 2):
        pair[0].gravity(pair[1])
    for moon in moons:
        moon.step()
tot = 0
for moon in moons:
    pot = abs(moon.x) + abs(moon.y) + abs(moon.z)
    kin = abs(moon.dx) + abs(moon.dy) + abs(moon.dz)
    tot += pot*kin
print(tot)
