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
    # returns the eight different transformations:
    # [
    #   rotated cw  mirrored through horizontal
    #   0           no
    #   1           no
    #   2           no
    #   3           no
    #   0           yes
    #   1           yes
    #   2           yes
    #   3           yes
    # ]
    tiles = []
    tiles.append(tile[:10])   # up
    tiles.append(tile[9::10]) # right
    tiles.append(tile[-10:])  # down
    tiles.append(tile[::10])  # left
    tiles = list(map(lambda r: int(r.replace("#", "1").replace(".", "0"), 2), tiles))

    tiles = rotations(tiles)
    # mirror through horizontal by
    #   flipping up and down
    #   mirroring left and right respectively
    tiles += [[tile[DOWN],           # up
               mirror(tile[RIGHT]),  # right
               tile[UP],             # down
               mirror(tile[LEFT])]   # left
              for tile in tiles]
    return tiles


def neighbours(p, w, h):
    # None if outside w, h
    return [
        (p[0], p[1]-1) if p[1]-1 >= 0 else None,
        (p[0]+1, p[1]) if p[0]+1 < w  else None,
        (p[0], p[1]+1) if p[1]+1 < h  else None,
        (p[0]-1, p[1]) if p[0]-1 >= 0 else None,
    ]


def valid(state, p, w, h):
    n = neighbours(p, w, h)
    # a neighbour is valid if any of the following:
    #   it's outside w, h
    #   it's inside w, h but not placed
    #   it's placed and its corresponding side matches this position's side
    return all((
        not n[UP] or n[UP] not in state or state[p][UP] == state[n[UP]][DOWN],
        not n[RIGHT] or n[RIGHT] not in state or state[p][RIGHT] == state[n[RIGHT]][LEFT],
        not n[DOWN] or n[DOWN] not in state or state[p][DOWN] == state[n[DOWN]][UP],
        not n[LEFT] or n[LEFT] not in state or state[p][LEFT] == state[n[LEFT]][RIGHT],
    ))


def next_pos(p, w):
    # like a typewriter
    x, y = p
    return ((x+1) % w, y + (x+1)//w)


def gen_image(_in, w, h):
    tile_borders = dict() # id: [sides as encoded numbers]
    tiles = dict()        # id: [rows as characters]
    for tile in "".join(_in)[:-1].split("\n\n"):
        num = int(tile.split("\n")[0].split(" ")[1][:-1])

        tile_borders[num] = all_tiles(tile[tile.find(":")+2:].replace("\n", ""))
        tiles[num] = tile[tile.find(":")+2:]

    def test(state, next, left, placed):
        # state: {(x, y): (UP, RIGHT, DOWN, LEFT)}
        # next: (x, y), next empty position
        # left: set(tile), tile indicies available
        # placed: [(tile, mod)], placed tiles and their modification id
        #
        # returns a valid state or None if none exist
        if not left:
            return state, placed

        for tile in left:
            for i, mod in enumerate(tile_borders[tile]):
                new = state.copy()
                new[next] = mod
                if valid(new, next, w, h):
                    test_res = test(new, next_pos(next, w), left - set([tile]), placed + [(tile, i)])
                    if test_res:
                        return test_res
        return None

    return test(dict(), (0, 0), set(tile_borders.keys()), []), tiles


def pt1(_in):
    res = gen_image(_in, 12, 12)[0][1]
    return res[0][0] * res[11][0] * res[-12][0] * res[-1][0]


def pt2(_in):
    image = gen_image(_in, 12, 12)

    def rotate_cw(mat, s):
        res = [[None for _ in range(s)] for _ in range(s)]
        for y in range(s):
            for x in range(s):
                res[x][s-y-1] = mat[y][x]
        return res

    def mirror(mat, s):
        res = [[None for _ in range(s)] for _ in range(s)]
        for y in range(s):
            for x in range(s):
                res[y][x] = mat[s-y-1][x]
        return res

    def mir_rot(mat, mod):
        for _ in range(mod % 4):
            mat = rotate_cw(mat, len(mat))
        for _ in range(mod // 4):
            mat = mirror(mat, len(mat))
        return mat

    def has_monster(image, x, y, w, h):
        monster = [
            "                  # ",
            "#    ##    ##    ###",
            " #  #  #  #  #  #   "
        ]
        for dy in range(len(monster)):
            img_y = y + dy
            if not 0 <= img_y < h:
                return False
            for dx in range(len(monster[dy])):
                img_x = x + dx
                if not 0 <= img_x < w:
                    return False
                if monster[dy][dx] == "#" and image[img_y][img_x] != "#":
                    return False
        return True

    # orient tiles
    tiles = [mir_rot(image[1][tile[0]].split("\n"), tile[1])
             for tile in image[0][1]]

    # remove borders
    tiles = [[row[1:-1]
              for row in tile[1:-1]]
             for tile in tiles]

    # build the total image
    total = []
    for tile_row in range(12):
        for row in range(8):
            total.append("".join(["".join(tiles[tile_row*12 + tile][row]) for tile in range(12)]))
    #TODO this should work
    # total = ["".join(["".join(tiles[tile_row*12 + tile][row])
    #                   for tile in range(12)])
    #          for row in range(8)
    #          for tile_row in range(12)]

    for mod in range(8):
        image = mir_rot(total, mod)
        h = len(image)
        w = len(image[0])
        monsters = sum(1 if has_monster(image, x, y, w, h) else 0
                       for x in range(w)
                       for y in range(h))
        if monsters != 0:
            return sum(row.count("#") for row in image) - monsters * 15


if __name__ == "__main__":
    _in = aoc20.read_input(sys.argv[1:], 20)
    print(pt1(_in))
    print(pt2(_in))
