with open("day08.txt") as file:
    instructions = file.read().splitlines()

import numpy as np
from copy import copy


def execute(instruction, acc, i):
    typ, nb = instruction.split()
    if typ == "nop":
        i += 1
    elif typ == "jmp":
        i += int(nb)
    elif typ == "acc":
        acc += int(nb)
        i += 1
    return acc, i


# part 1
acc, i = 0, 0
instruction_processed = np.zeros(len(instructions))

while instruction_processed[i] == 0:
    instruction_processed[i] = 1
    acc, i = execute(instructions[i], acc, i)

print(acc)
# part 2

def run_with_changes(instructions, j):

    typ, nb = instructions[j].split()
    if typ == "acc":
        pass
    elif typ =="nop":
        instructions[j] = str("jmp " + nb)
    else:
        instructions[j] = str("nop " + nb)

    acc, i = 0, 0
    instruction_processed = np.zeros(len(instructions))

    try:
        while instruction_processed[i] == 0:
            instruction_processed[i] = 1
            acc, i = execute(instructions[i], acc, i)
        return 0

    except IndexError:
        print(acc)
        return 0

for j in range(len(instructions)):
    run_with_changes(copy(instructions), j)
    