with open("day10.txt") as file:
    joltages = sorted([int(i) for i in file.read().splitlines()])

prev = 0
diffof1 = 0
diffof3 = 0

for joltage in joltages:
    if joltage - prev == 1:
        diffof1 += 1
    elif joltage - prev == 3:
        diffof3 += 1
    prev = joltage

diffof3 = diffof3+1 # difference with final output
print((diffof3+1)*diffof1)

