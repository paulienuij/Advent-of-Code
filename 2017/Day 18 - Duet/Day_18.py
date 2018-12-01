def separate(instr):
    global alphabet
    inst =  instr[0]

    x = instr[1]
    if x not in alphabet:
        x = int(x)

    if inst not in ['snd', 'rcv']:
        y = instr[2]
        if y not in alphabet:
            y = int(y)
        return inst, x, y

    else:
        return inst, x, "none"

file = open(r"data.txt", "r", encoding="utf-8-sig")
lines = file.readlines()

instructions = []
registeries = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for line in lines:
    instruction = line.split()
    if instruction[1] not in registeries.keys() and instruction[1] in alphabet:
        registeries[instruction[1]]= 0
    instructions.append(instruction)

while True:
    inst, x, y = separate(instructions[i])

    if inst == "snd":
        if not isinstance(x, int):
            x = registeries[x]
        last_snd = x

    elif inst == "set":
        if not isinstance(y, int):
            y = registeries[y]
        registeries[x] = y

    elif inst == "add":
        if not isinstance(y, int):
            y = registeries[y]
        registeries[x] += y

    elif inst == "mul":
        if not isinstance(y, int):
            y = registeries[y]
        registeries[x] *= y

    elif inst == "mod":
        if not isinstance(y, int):
            y = registeries[y]
        registeries[x] %= y

    elif inst == "rcv":
        if not isinstance(x, int):
            x = registeries[x]
        if x != 0:
            break

    elif inst == "jgz":
        if not isinstance(x, int):
            x = registeries[x]
        if not isinstance(y, int):
            y = registeries[y]
        if x > 0:
            i = i + y - 1

    i += 1

print('the frequency of the last played sound is ', last_snd)

