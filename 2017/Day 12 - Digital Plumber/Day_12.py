import numpy as np

file = open(r"data.txt", "r", encoding="utf-8-sig")
lines = file.readlines()

linked_to_zero = [0]
length_changes = 0
last_len = 1

while length_changes < 10:
    for line in lines:
        link = int(line.split(' <-> ')[0])
        if link in linked_to_zero:
            linked_to_zero += [int(x) for x in line.split(' <-> ')[1].split(',')]
    linked_to_zero = list(set(linked_to_zero))
    if len(linked_to_zero) == last_len:
        length_changes += 1
    else:
        last_len = len(linked_to_zero)

print(len(linked_to_zero))


