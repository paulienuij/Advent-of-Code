file = open(r"data.txt", "r", encoding="utf-8-sig")
lines = file.readlines()


class Program:
    def __init__(self, name, weight, carried_programmes):
        self.name = name
        self.weight = weight
        self.carried_programmes = carried_programmes
        self.carried_weight = []
        for i in range(len(carried_programmes)):
            self.carried_weight.append("-")

programmes = []

for line in lines:

    name = line.split()[0]
    weight = int(line.split("(")[1].split(")")[0])
    carried_pgms = []

    if "->" in line:
        top_pgms = line.split("> ")[1].split('\n')[0].split(", ")
        for pgm in top_pgms:
            carried_pgms.append(pgm)

    programmes.append(Program(name, weight, carried_pgms))

print('list of programmes ready!')

while True:

    for pgm1, pgm2 in zip(programmes, programmes):

        # if pgm1 carries no programmes and pgm2 carries pgm 1
        if pgm1.carried_programmes == [] and pgm1.name in pgm2.carried_programmes:

            #correct pgm1's weight in pgm2 and femove pgm1 from list of programmes
            i = pgm2.carried_programmes.index(pgm1.name)
            pgm2.carried_programmes[i] = pgm1.weight
            programmes.remove(pgm1m)

            print("weight corrected")

            # check if pgm2 carries any progammes whose names have not been changed to weights
            if all(isinstance(x,int)for x in pgm[2:]):

                #if all weights are identical
                if len(set(list(pgm2.carried_programmes)))==1:
                    #replace tower by 1 pgm of the weight of the whole tower
                    new_weight = pgm2.weight + sum(pgm2.carried_programmes)
                    pgm2 = Program(pgm2.name, new_weight, [])
                    print(pgm2.name + " has been found non guilty")

                #else, we have found the culprit!
                else:
                    print(pgm2.carried_programmes, pgm2.carried_weight)
                    break
