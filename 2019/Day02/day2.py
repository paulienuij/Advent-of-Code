import copy
import itertools


with open("input.txt") as file:
    code = [int(c) for c in file.read().split(",")]


def intcode(noun, verb, c):
    code = copy.copy(c)
    code[1] = noun
    code[2] = verb
    i = 0
    while code[i] != 99:
        if code[i] == 1: # opcode for addition
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
        elif code[i] == 2: # opcode for multiplication
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
        i += 4
    return code[0]


print("part1:", intcode(12, 2, code))

for n, v in itertools.product(range(100), repeat=2):
    if intcode(n, v, code) == 19690720:
        print("part2:", 100*n+v)
        break






