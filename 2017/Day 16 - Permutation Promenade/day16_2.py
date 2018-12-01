file = open(r"data.txt", "r", encoding="utf-8-sig")
moves = file.read().split(",")

def dance(danceline, moves):

    spin = "s"
    exchange = "x"
    partner = "p"
    l = len(danceline)

    for move in moves:

        if move[0] == spin:
            spin_size = int(move[1:])
            end = danceline[(l-spin_size):]
            front = danceline[:(l-spin_size)]
            danceline = end + front
        elif move[0] == exchange:
            #xA/B, makes the programs at positions A and B swap
            posA, posB = map(int, move[1:].split("/"))
            A = danceline[posA]
            B = danceline[posB]
            danceline[posA] = B
            danceline[posB] = A
        elif move[0] == partner:
            #pA/B: makes the programs named A and B swap places.
            A, B = move[1:].split("/")
            posA = danceline.index(A)
            posB = danceline.index(B)
            danceline[posA] = B
            danceline[posB] = A

    return danceline

danceline = []
for program in 'abcdefghijklmnop':
    danceline.append(program)

prev_lines = []

while True:
    danceline = dance(danceline, moves)

    if danceline in prev_lines:
        break
    else:
        prev_lines.append(list(danceline))


danceline_1bill = prev_lines[1000000000%(len(prev_lines)-3)]

line = ""
for program in danceline_1bill:
    line += program



print(line)
