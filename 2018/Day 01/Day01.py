# part 1
with open("data.txt") as file:
    f_changes = file.read().splitlines()

f = 0
for change in f_changes:
    f += int(change)

print(f)

# part 2
f = [0]
repeatFound = False

while not repeatFound:
    for change in f_changes:
        new_f = f[-1] + int(change)
        if new_f in f:
            print(new_f)
            repeatFound = True
        f.append(new_f)

print(f[-1])

