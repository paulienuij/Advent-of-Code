with open("data.txt") as file:
    box_IDs = file.read().splitlines()

#part 1
nb_doubles = 0
nb_triples =0

for ID in box_IDs:
    doubles = [x for n, x in enumerate(ID) if x in ID[:n]]
    triples = [x for n, x in enumerate(doubles) if x in doubles[:n]]

    #remove the triples from the doubles
    doubles = [ x for x in doubles if x not in triples]

    if len(doubles) > 0.5:
        nb_doubles += 1
    if len(triples) > 0.5:
        nb_triples += 1

print(nb_triples*nb_doubles)

