'''
the progamr loopr between instruction 11 and 19
first 5 loops:
{'c': 125100, 'f': 1, 'h': 0, 'd': 2, 'b': 108100, 'g': -108097, 'e': 3, 'a': 1}
{'c': 125100, 'f': 1, 'h': 0, 'd': 2, 'b': 108100, 'g': -108096, 'e': 4, 'a': 1}
{'c': 125100, 'f': 1, 'h': 0, 'd': 2, 'b': 108100, 'g': -108095, 'e': 5, 'a': 1}
{'c': 125100, 'f': 1, 'h': 0, 'd': 2, 'b': 108100, 'g': -108094, 'e': 6, 'a': 1}
{'c': 125100, 'f': 1, 'h': 0, 'd': 2, 'b': 108100, 'g': -108093, 'e': 7, 'a': 1}

it will get out looking as follows:
{'c': 125100, 'f': 1, 'h': 0, 'd': 2, 'b': 108100, 'g': 0, 'e': 108100, 'a': 1}
'''

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
loop = 0

for line in lines:
    instruction = line.split()
    if instruction[1] not in registeries.keys() and instruction[1] in alphabet:
        registeries[instruction[1]]= 0
    instructions.append(instruction)

registeries["a"]=1

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

        if i == 19 : #and loop < 6:
            loop +=1
            print(registeries)
        if loop == 5:
            print('...')
            registeries["g"] = 0
            registeries["e"] = 108100
            i = 20
            print(registeries)
            loop =6

        #print(i)
        #print(registeries)
        #print(registeries["g"], registeries["e"])

    except IndexError :
        #print(i)
        break

print("the final value in h is: ", registeries["h"] )

