import numpy as np
from itertools import product

with open('input.txt') as file:
    img = file.read().splitlines()[0]


w = 25
h = 6

nblayers = int(len(img)/(w*h))
layers ={}
min_zeros = w*h
index = -1

# part1
for i in range(nblayers):
    layers[i] = img[w*h*i:w*h*(i+1)]
    zeros = layers[i].count("0")
    if zeros < min_zeros:
        min_zeros = zeros
        index = i

ones = layers[index].count("1")
twos = layers[index].count("2")

print(ones*twos)

# part2
pic = np.full((h, w), 2)

for i in range(nblayers):
    for x, y in product(range(h), range(w)):
        if pic[x, y] == 2:
            pic[x, y] = layers[i][x*w+y]

for x in range(h):
    row = ""
    for y in range(w):
        if pic[x, y] == 1:
            row = row + " X "
        else:
            row = row + "   "
    print(row)



