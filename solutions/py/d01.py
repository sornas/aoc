import math
import sys

def get_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    return 0 if fuel <= 0 else fuel + get_fuel(fuel)

def pt1(_in):
    s = 0
    for line in _in:
        mass = int(line)
        if mass == 0:
            break
        fuel = math.floor(mass / 3) - 2
        s += fuel
    return s

def pt2(input):
    return sum([get_fuel(int(line)) for line in input])
