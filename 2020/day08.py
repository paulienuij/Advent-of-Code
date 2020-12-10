import numpy as np
from copy import copy


with open("day08.txt") as file:
    instructions = file.read().splitlines()


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

for j in range(len(instructions)):
    instr = copy(instructions)
    typ, nb = instructions[j].split()

    # change instruction j
    if typ == "acc":
        pass
    elif typ == "nop":
        instr[j] = str("jmp " + nb)
    else:
        instr[j] = str("nop " + nb)

    # run the instructions until the index is out of range
    acc, i = 0, 0
    instruction_processed = np.zeros(len(instructions))
    try:
        while instruction_processed[i] == 0:
            instruction_processed[i] = 1
            acc, i = execute(instr[i], acc, i)

    except IndexError:
        print(acc)

