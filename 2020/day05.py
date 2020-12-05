with open("day05.txt") as file:
    rows = file.read().splitlines()


def splitrange(b, t , type):
    l = int((t-b)/2)
    if type == "F" or type =="L":
        return b, b+l
    else:
        return b+l+1, t

ids = []

for seat in rows:
    b, t = 0, 127
    for c in seat[:7]:
        b, t = splitrange(b, t, c)
    row = b

    b, t = 0, 7
    for c in seat[7:]:
        b, t = splitrange(b, t, c)
    col = b
    id = row * 8 + col
    ids.append(id)

print(max(ids))

for i in range(max(ids)):
    if i not in ids:
        print(i)
