def count(layer, num):
    return sum([row.count(num) for row in layer])

def pt1(input):
    img = []
    least_zeroes = 150  # max
    n = 0
    for l in range(100):
        layer = [[int(input[0][l*25*6 + y*25 + x]) for x in range(25)] for y in range(6)]
        if count(layer, 0) < least_zeroes:
            least_zeroes = count(layer, 0)
            n = count(layer, 1) * count(layer, 2)
        img.append(layer)
    return n

def pt2(input):
    img = [[[int(input[0][l*25*6 + y*25 + x]) for x in range(25)] for y in range(6)] for l in range(100)]
    result = img[0]
    for layer in img[1:]:
        for x in range(25):
            for y in range(6):
                if result[y][x] == 2:
                    result[y][x] = layer[y][x]
    str_res = []
    for row in result:
        for c in row:
            str_res.append('\u2588' if c == 1 else ' ')
        str_res.append("\n")
    return "\n" + ("".join(str_res))

if __name__ == "__main__":
    import cProfile

    input = open("../input/08", "r").readlines()
    cProfile.run("pt1(input)")
    cProfile.run("pt2(input)")
    print(pt1(input))
    print(pt2(input))
