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

# Each joltage route is equal to the sum of the number of routes to the previous three joltages.
# However, some of the joltages won't be present in the list of adaptors.
# So the number of routes to them will be 0.
routes = {}
routes[0] = 1
for j in joltages:
    routes[j] = routes.get(j-1, 0) + routes.get(j-2, 0) + routes.get(j-3, 0)

print(f"Part 2: {routes[max(routes.keys())]}")