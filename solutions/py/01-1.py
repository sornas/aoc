import math
import sys

s = 0
for line in sys.stdin:
    mass = int(line)
    if mass == 0:
        break
    fuel = math.floor(mass / 3) - 2
    s += fuel
    print("adding", fuel)
    print("at", s)
print("sum", s)
