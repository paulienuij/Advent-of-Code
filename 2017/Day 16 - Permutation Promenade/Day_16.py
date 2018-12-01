file = open(r"data.txt", "r", encoding="utf-8-sig")
moves = file.read().split(",")

danceline = []

names = 'abcdefghijklmnop'
#names = 'abcde'

for program in names:
    danceline.append(program)

spin = "s"
exchange = "x"
partner = "p"

l = len(danceline)

for move in moves:
#for move in ['s1', 'x3/4', 'pe/b' ]:

   if move[0] == spin:
       spin_size = int(move[1:])
       end = danceline[(l-spin_size):]
       front = danceline[:(l-spin_size)]
       danceline = end + front

   elif move[0] == exchange:
       #xA/B, makes the programs at positions A and B swap
       posA, posB = move[1:].split("/")
       posA = int(posA)
       posB = int(posB)
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


line = ""
for program in danceline:
    line += program

print(line)