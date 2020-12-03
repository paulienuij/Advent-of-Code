from itertools import combinations

with open("day01.txt") as file:
    numbers = [int(n) for n in file.read().splitlines()]

for n, m in combinations(numbers, 2):
    if n+m == 2020:
        print(n*m)
        break

for n, m, o in combinations(numbers, 3):
    if n+m+o == 2020:
        print(n*m*o)
        break
