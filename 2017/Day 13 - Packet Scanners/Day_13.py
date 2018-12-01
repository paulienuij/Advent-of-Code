file = open(r"data.txt", "r", encoding="utf-8-sig")
lines = file.readlines()

severity_1 = 0

for line in lines:
    data = line.split(": ")
    layer = int(data[0])
    range = int(data[1])
    if layer % ((range-1)*2) == 0:
            severity_1 += (layer*range)

found = False
n = 0
length = len(lines)

print("Part 1: ", severity_1)

while found == False and n < 16493811:
    n += 1
    catched = False
    for line in lines:
        data = line.split(": ")
        layer = int(data[0])
        range = int(data[1])
        if (layer+n) % ((range-1)*2) == 0:
            catched = True
            break

    if catched == False:
        found = True

print("Part 2: ", n)
