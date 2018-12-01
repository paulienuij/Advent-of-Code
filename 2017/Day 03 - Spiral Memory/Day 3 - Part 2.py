import numpy as np
import itertools

np.set_printoptions(suppress=True, linewidth=200)

def move_right(x, y):
    return x, y+1

def move_down(x, y):
    return x+1, y

def move_left(x, y):
    return x, y-1

def move_up(x, y):
    return x-1, y


def sum_around(spiral, x_0, y_0):
    global step
    total = spiral[x_0-1, y_0-1] + spiral [x_0-1, y_0] + spiral[x_0-1, y_0+1] + \
            spiral[x_0  , y_0-1] + spiral [x_0  , y_0] + spiral[x_0  , y_0+1] + \
            spiral[x_0+1, y_0-1] + spiral [x_0+1, y_0] + spiral[x_0+1, y_0 + 1]
    step += 1
    return total
'''

def sum_around(spiral, x_0, y_0):
    #used to test fo correct spiraling
    global step
    step += 1
    #print(spiral)
    return step
'''

input_dat = 368078
step = 1

x_range = 12
y_range = 12

spiral = np.zeros((x_range, y_range))
x = int(x_range/2)
y = int(y_range/2)
spiral[x, y] = 1

N = 1

try:
    while np.amax(spiral) <= input_dat:
        # figure out how to spiral
        #based on https://stackoverflow.com/questions/23706690/how-do-i-make-make-spiral-in-python
        for n in range(N):
            x, y = move_right(x, y)
            spiral[x, y] = sum_around(spiral, x, y)
        for  n in range(N):
            x, y = move_up(x, y)
            spiral[x, y] = sum_around(spiral, x, y)
        for n in range(N+1):
            x, y = move_left(x, y)
            spiral[x, y] = sum_around(spiral, x, y)
        for n in range(N+1):
            x, y = move_down(x, y)
            spiral[x, y] = sum_around(spiral, x, y)
        N += 2

except IndexError:
    pass

morethaninput = []
for x in range (x_range):
    for y in range(y_range):
        if spiral[x, y] >= input_dat:
            morethaninput.append(spiral[x, y])


print(spiral)
print(min(morethaninput))


