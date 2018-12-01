file = open(r"data.txt", "r", encoding="utf-8-sig")
line = file.read()

garbage = False
skip = False
score = 0
indent = 0
nb_garb = 0

for c in line:
    if skip:
        skip = False
        continue

    elif c == "!":
        skip = True
        continue

    elif c == ">":
        garbage = False

    elif garbage:
        nb_garb +=1
        continue

    elif c == "<":
        garbage = True

    elif c == "{":
        indent += 1
        score += indent

    elif c == "}":
        indent -= 1

print(score)
print(nb_garb)



