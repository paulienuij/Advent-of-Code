import copy
import itertools


with open("input.txt") as file:
    code = [int(c) for c in file.read().split(",")]


def intcode(noun, verb, c):
    code = copy.copy(c)
    code[1], code[2] = noun, verb
    i = 0
    while True:
        opcode = code[i]
        i1, i2, i3 = code[i+1], code[i+2], code[i+3]
        if opcode == 1:  # opcode for addition
            code[i3] = code[i1] + code[i2]
        elif opcode == 2:  # opcode for multiplication
            code[i3] = code[i1] * code[i2]
        elif opcode == 99:  # opcode for stopping
            return code[0]
        else:
            print("unknown opcode")
            return 0
        i += 4


print("part1:", intcode(12, 2, code))

for n, v in itertools.product(range(100), repeat=2):
    if intcode(n, v, code) == 19690720:
        print("part2:", 100*n+v)
        break






