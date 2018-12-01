file = open(r"data.txt", "r", encoding="utf-8-sig")
lines = file.readlines()

registeries = {}  # this is a dictionary

instructions = []
conditions = []
maximum_2 = 0

class Condition:
    def __init__(self, var, sign, value):
        self.var = var
        self.sign = sign
        self.value = int(value)

    def true(self, reg):
        if self.sign == "==":
            return reg[self.var] == self.value
        elif self.sign == "!=":
            return reg[self.var] != self.value
        elif self.sign == ">":
            return reg[self.var] > self.value
        elif self.sign == ">=":
            return reg[self.var] >= self.value
        elif self.sign == "<":
            return reg[self.var] < self.value
        elif self.sign == "<=":
            return reg[self.var] <= self.value
        else:
            print("unknown sign: ", self.sign)


class Instruction:
    def __init__(self, var, sign, value):
        self.var = var
        if sign == 'inc':
            self.value = int(value)
        else:
            self.value = -int(value)

    def apply(self, reg):
        return reg[self.var] + self.value


for line in lines:
    name = line.split()[0]
    registeries[name] = 0

for line in lines:
    statement = line.split(' if ')
    var, sign, value = statement[1].split()
    conditions.append(Condition(var, sign, value))

    var, sign, value = statement[0].split()
    instructions.append(Instruction(var, sign, value))

for i in range(len(instructions)):
    if conditions[i].true(registeries):
        var = instructions[i].var
        new_value = instructions[i].apply(registeries)
        registeries[var] = new_value
        maximum_2 = max(maximum_2, new_value)


maximum_1 = max(registeries, key=registeries.get)
print(maximum_1, registeries[maximum_1])
print(maximum_2)
