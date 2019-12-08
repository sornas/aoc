import d01
import d02
import d03
import d04
import d05
import d06
import d07
import d08

mods = [d01, d02, d03, d04, d05, d06, d07, d08]

for mod, day in zip(mods, range(8)):
    print("Day", str(day+1).zfill(2))
    print("Part", 1, mod.pt1(open("../input/" + str(day+1).zfill(2), "r").readlines()))
    print("Part", 2, mod.pt2(open("../input/" + str(day+1).zfill(2), "r").readlines()))
