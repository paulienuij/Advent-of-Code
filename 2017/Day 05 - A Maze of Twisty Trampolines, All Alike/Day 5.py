file = open(r"data.txt", "r", encoding="utf-8-sig")
data = file.readlines()

program = []
for number in data:
    program.append(int(number))

steps = 0
i = 0

while i < len(program):
    jump = program[i]
    program[i] = program[i]+1
    i = i + jump
    steps += 1

print(steps)
