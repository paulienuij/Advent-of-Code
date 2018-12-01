'''

Using cube coordinates for hexagon lattices
https://www.redblobgames.com/grids/hexagons/#distances-cube
'''

file = open(r"data.txt", "r", encoding="utf-8-sig")
path = file.read().split(",")

x = 0
y = 0
z = 0

maximum = 0

for step in path:
    if step == "n":
        y += 1
        x -= 1
    elif step == "ne":
        y += 1
        z -= 1
    elif step == "nw":
        x -= 1
        z += 1
    elif step == "s":
        x += 1
        y -= 1
    elif step == "se":
        x += 1
        z -= 1
    elif step == "sw":
        z += 1
        y -= 1
    current = (abs(x) + abs(y) + abs(z)) / 2
    maximum = max(maximum, current)

print((abs(x) + abs(y) + abs(z)) / 2 )
print(maximum)


