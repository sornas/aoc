import aoc20
import sys
import itertools


UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3


def mirror(n):
    return int(bin(n)[2:].zfill(10)[::-1], 2)


def rotations(lst):
    def rotate_cw(lst):
        return [
            mirror(lst[LEFT]),  # up
            lst[UP],            # right
            mirror(lst[RIGHT]), # down
            lst[DOWN]]          # left

    lst = [lst]
    for _ in range(3):
        lst += [rotate_cw(lst[-1])]
    return lst


def all_tiles(tile):
    # assumes 10x10 tile as 100 chars
    tiles = []
    tiles.append(tile[:10]) # top
    tiles.append(tile[9::10]) # right
    tiles.append(tile[-10:]) # bottom
    tiles.append(tile[::10]) # left
    tiles = list(map(lambda r: int(r.replace("#", "1").replace(".", "0"), 2), tiles))

    tiles = rotations(tiles)
    tiles += [[tile[DOWN], mirror(tile[RIGHT]), tile[UP], mirror(tile[LEFT])]
              for tile in tiles]
    return tiles


def neighbours(p, w, h):
    return [
        (p[0], p[1]-1) if p[1]-1 >= 0 else None,
        (p[0]+1, p[1]) if p[0]+1 < w else None,
        (p[0], p[1]+1) if p[1]+1 < h else None,
        (p[0]-1, p[1]) if p[0]-1 >= 0 else None,
    ]


def valid(state, p, w, h):
    n = neighbours(p, w, h)
    res = all((
        not n[UP] or n[UP] not in state or state[p][UP] == state[n[UP]][DOWN],
        not n[RIGHT] or n[RIGHT] not in state or state[p][RIGHT] == state[n[RIGHT]][LEFT],
        not n[DOWN] or n[DOWN] not in state or state[p][DOWN] == state[n[DOWN]][UP],
        not n[LEFT] or n[LEFT] not in state or state[p][LEFT] == state[n[LEFT]][RIGHT],
    ))
    return res


def next_pos(p, w):
    x, y = p
    return ((x+1) % w, y + (x+1)//w)


def pt1(_in):
    w = h = 12
    tiles = dict()
    for tile in "".join(_in).split("\n\n"):
        num = int(tile.split("\n")[0].split(" ")[1][:-1])

        tiles[num] = all_tiles(tile[tile.find(":")+1:].replace("\n", ""))

    def test(state, next, left, placed):
        # state: {(x, y): (UP, RIGHT, DOWN, LEFT)}
        # next: (x, y), next empty position
        # left: set(tile), tile indicies available
        if not left:
            return state, placed

        for tile in left:
            for mod in tiles[tile]:
                new = state.copy()
                new[next] = mod
                if valid(new, next, w, h):
                    test_res = test(new, next_pos(next, w), left - set([tile]), placed + [tile])
                    if test_res:
                        return test_res

    res = test(dict(), (0, 0), set(tiles.keys()), [])[1]
    return res[0] * res[11] * res[-12] * res[-1]


def pt2(_in):
    pass


if __name__ == "__main__":
    _in = aoc20.read_input(sys.argv[1:], 20)
    print(pt1(_in))
    print(pt2(_in))
