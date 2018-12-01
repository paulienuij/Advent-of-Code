cycle_data = [4, 1,	15,	12,	0, 9, 9, 5,	5, 8, 7, 3,	14,	5, 12, 3]
l = len(cycle_data)
previous_cycles = []

while True:
    if cycle_data in previous_cycles:
        break
    else:
        previous_cycles.append(list(cycle_data))
        n = max (cycle_data)
        i = cycle_data.index(n)

        cycle_data[i] = 0
        for j in range(i+1, i+n+1):
            cycle_data[j%l] += 1

print(len(previous_cycles))
print(len(previous_cycles)-previous_cycles.index(cycle_data))

