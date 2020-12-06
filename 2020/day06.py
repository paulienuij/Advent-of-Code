with open("day06.txt") as file:
    groups = file.read().split("\n\n")

sum = 0
for group in groups:
    sum = sum+len(set(group.replace("\n", "")))

print(sum)

sum = 0
for group in groups:
    answ = group.split("\n")
    questions = set(group.replace("\n", ""))
    for letter in questions:
        if all([letter in ans for ans in answ]):
            sum = sum+1

print(sum)
