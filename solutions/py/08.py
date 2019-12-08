f = open("../input/08", "r").readline()

def format(layers):
    i = 0
    for layer in layers:
        print("\nlayer", i)
        i += 1
        for row in layer:
            for c in row:
                print(c, end=' ')
            print("")

def count(layer, num):
    return sum([row.count(num) for row in layer])

img = []
least_zeroes = None
num = 0

for l in range(100):
    #print("l", l)
    layer = [[int(f[l*25*6 + y*25 + x]) for x in range(25)] for y in range(6)]
    zeroes = 0
    ones = 0
    twos = 0
    if least_zeroes == None:
        least_zeroes = count(layer, 0)
        num = count(layer, 1) * count(layer, 2)
    elif count(layer, 0) < least_zeroes:
        least_zeroes = count(layer, 0)
        num = count(layer, 1) * count(layer, 2)
    img.append(layer)
print(1, num)

def pretty(result):
    for row in result:
        for c in row:
            print(('\u2588' if c == 1 else ' '), end='')
        print("")

result = img[0]

for layer in img[1:]:
    for x in range(25):
        for y in range(6):
            if result[y][x] == 2:
                result[y][x] = layer[y][x]
print(2)
pretty(result)
