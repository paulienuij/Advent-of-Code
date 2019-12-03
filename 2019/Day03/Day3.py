import numpy as np

with open("input.txt") as file:
    wires = file.read().splitlines()
print(wires)
d = {"U": np.array([1, 0]), "D": np.array([-1, 0]), "R": np.array([-1, 0]), "L": np.array([-1, 0])}


def coordinates(wire):
    length = []
    points = []
    p = np.array([0,0])
    l = 0
    for w in wire:
        di = w[0]
        r = int(w[1:])
        for _ in range(r):
            p += d[di]
            l += 1
            lp = list(p)
            if lp not in points:
                points.append(lp)
                length.append(l)

    return points, length


p0, l0 = coordinates(wires[0].split(","))
p1, l1 = coordinates(wires[1].split(","))

overlap = [sum(p) for p in p0 if p in p1]
print(min(overlap))