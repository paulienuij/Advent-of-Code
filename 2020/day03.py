with open("day03.txt") as file:
    rows = file.read().splitlines()


def treesforslope(a, b):
    trees = 0
    width = len(rows[0])
    for i in range(len(rows)):
        if i%a == 0:
            char = rows[i][(b*i)%width]
            if char == "#":
                trees += 1
    return trees

# part 1
print(treesforslope(1, 3))

# part 2
print(treesforslope(1, 1) * treesforslope(1, 3) *
      treesforslope(1, 5) * treesforslope(1, 7) *
      treesforslope(2, 1))
