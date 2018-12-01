file = open(r"data.txt", "r", encoding="utf-8-sig")

lines = file.readlines()

carrying_programmes = []
carried_programmes = []


#remove all top progammes carrying no other programmes
for line in lines:
    if "->" in line:
        bottom_pgm = line.split(" (")[0]
        carrying_programmes.append(bottom_pgm)
        top_pgms = line.split("> ")[1].split('\n')[0].split(", ")
        for pgm in top_pgms:
            carried_programmes.append(pgm)

for programme in carrying_programmes:
    if programme not in carried_programmes:
        print (programme)

