import aoc20
import sys


def pt1(_in):
    door_public = int(_in[0])
    card_public = int(_in[1])

    val = 1
    door_ls = 0
    while val != door_public:
        door_ls += 1
        val = (val * 7) % 20201227

    val = 1
    card_ls = 0
    while val != card_public:
        card_ls += 1
        val = (val * 7) % 20201227

    val = 1
    for _ in range(door_ls):
        val = (val * card_public) % 20201227
    return val


def pt2(_in):
    pass


if __name__ == "__main__":
    _in = aoc20.read_input(sys.argv[1:], 25)
    print(pt1(_in))
    print(pt2(_in))
