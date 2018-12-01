class Program:

    def __init__(self, instructions, reg, nb):
        self.i = 0
        self.used = False
        self.received = False
        self.reg = reg
        self.reg["p"] = nb
        self.instruction = instructions
        self.finished = False
        self.l = len(instructions)

    def execute(self, rcv):
        self.used = False

        while True:
            if self.i > self.l:
                self.finished = True
                break

            inst, x, y = self.separate(self.instruction[self.i])

            if inst == "snd":
                if not isinstance(x, int):
                    x = self.reg[x]
                return x, self.i

            elif inst == "set":
                if not isinstance(y, int):
                    y = self.reg[y]
                self.reg[x] = y

            elif inst == "add":
                if not isinstance(y, int):
                    y = self.reg[y]
                self.reg[x] += y

            elif inst == "mul":
                if not isinstance(y, int):
                    y = self.reg[y]
                self.reg[x] *= y

            elif inst == "mod":
                if not isinstance(y, int):
                    y = self.reg[y]
                self.reg[x] %= y

            elif inst == "rcv":
                if self.received:
                    break
                elif not self.used:
                    self.reg[x] = rcv
                    self.received = True
                else:
                    break

            elif inst == "jgz":
                if not isinstance(x, int):
                    x = self.reg[x]
                if not isinstance(y, int):
                    y = self.reg[y]
                if x > 0:
                    self.i = self.i + y - 1

            self.i += 1

    @staticmethod
    def separate(instr):
        alphabet_ = 'abcdefghijklmnopqrstuvwxyz'
        inst = instr[0]

        x = instr[1]
        if x not in alphabet_:
            x = int(x)

        if inst not in ['snd', 'rcv']:
            y = instr[2]
            if y not in alphabet_:
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

p_0 = Program(instructions, registeries, 0)
p_1 = Program(instructions, registeries, 1)

rcv = False
count = 0

while (not p_0.finished) or (not p_1.finished):
        rcv = p_0.execute(rcv)
        print(rcv)
        p_1.received = True
        rcv = p_1.execute(rcv)
        print(rcv)
        count += 1
        p_1.received = True
        print(p_1.i, p_0.i)

print(count)
