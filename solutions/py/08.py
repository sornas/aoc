def count(layer, num):
    return sum([row.count(num) for row in layer])

f = open("../input/08", "r").readline()
img = []
least_zeroes = 150  # 25*6
n = 0

for l in range(100):
    #print("l", l)
    layer = [[int(f[l*25*6 + y*25 + x]) for x in range(25)] for y in range(6)]
    if count(layer, 0) < least_zeroes:
        least_zeroes = count(layer, 0)
        n = count(layer, 1) * count(layer, 2)
    img.append(layer)
print(1, n)

result = img[0]
for layer in img[1:]:
    for x in range(25):
        for y in range(6):
            if result[y][x] == 2:
                result[y][x] = layer[y][x]
print(2)
for row in result:
    for c in row:
        print(('\u2588' if c == 1 else ' '), end='')
    print("")
