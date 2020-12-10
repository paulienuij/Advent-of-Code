import numpy as np
from itertools import combinations

with open("day09.txt") as file:
    numbers = [int(i) for i in file.read().splitlines()]

i = 25

Found = False
invalidnb = 0

while not Found:
    nb = numbers[i]
    sumrange = numbers[i-25:i]
    summable = False
    for n, m in combinations(sumrange, 2):
        if n+m == nb:
            summable = True

    if not summable:
        invalidnb = nb
        print(nb)
        Found = True
    else:
        i += 1

for i in range(len(numbers)):
    nb = numbers[i]
    j = 1
    while nb < invalidnb:
        try:
            nb = sum(numbers[i:i+j])
        except IndexError:
            break

        if nb == invalidnb:
            sumrange = numbers[i:i+j]
            print(min(sumrange)+max(sumrange))
            break
        j += 1





