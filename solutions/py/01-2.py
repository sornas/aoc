import math
import sys

def get_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + get_fuel(fuel)

fuels = []
for line in sys.stdin:
    if line.rstrip() == "":
        break
    fuels.append(get_fuel(int(line)))

print(sum(fuels))
