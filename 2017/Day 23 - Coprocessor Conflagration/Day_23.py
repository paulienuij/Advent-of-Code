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
i=0
mul = 0

for line in lines:
    instruction = line.split()
    if instruction[1] not in registeries.keys() and instruction[1] in alphabet:
        registeries[instruction[1]]= 0
    instructions.append(instruction)

while True:
    try:
        inst, x, y = separate(instructions[i])

        if inst == "set":
            if not isinstance(y, int):
                y = registeries[y]
            registeries[x] = y

        elif inst == "sub":
            if not isinstance(y, int):
                y = registeries[y]
            registeries[x] -= y

        elif inst == "mul":
            if not isinstance(y, int):
                y = registeries[y]
            registeries[x] *= y
            mul += 1

        elif inst == "jnz":
            if not isinstance(x, int):
                x = registeries[x]
            if not isinstance(y, int):
                y = registeries[y]
            if x != 0:
                i = i + y - 1

        i += 1
        #print(inst, x, y)
        #print(registeries)
    except IndexError :
        print(i)
        break

print("mul has been invoked ", mul, " times" )

