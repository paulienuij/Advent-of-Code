import numpy as np

with open('input.txt') as file:
    wires = file.read().splitlines()

di = {'L': np.array([-1, 0]), 'R': np.array([1, 0]), 'U': np.array([0, 1]), 'D': np.array([0, -1])}


def points_in_wire(wire):
    w = wire.split(",")
    points = []
    lengths = []
    length = 0
    p = np.array([0, 0])
    for c in w:
        d = c[0]
        l = int(c[1:])
        for j in range(l):
            p += di[d]
            p_ = list(p)
            length += 1
            if p_ not in points:
                points.append(p_)
                lengths.append(length)
        print('hi')
    return points, lengths

p0, l0 = points_in_wire(wires[0])
print('hey')
p1, l1 = points_in_wire(wires[1])
print('hey')
overlap = [abs(x[0]) + abs(x[1]) for x in p1 if x in p0]
print(min(overlap))
print(min([l0[p0.index(point)] + l1[p1.index(point)] for point in p0 if point in p1]))