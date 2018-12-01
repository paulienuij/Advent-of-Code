import itertools
import collections
file = open(r"data.txt", "r", encoding="utf-8-sig")

passphrases = file.readlines()
nb_passphrases = 0
nb_passphrases_2 = 0
valid_passphrases = []

for passphrase in passphrases:
    words = passphrase.split()
    length_0 = len(words)
    length_1 = len(list(set(words)))
    if length_0 == length_1:
        nb_passphrases += 1
        valid_passphrases.append(passphrase)

for passphrase in valid_passphrases:
    words = passphrase.split()
    rearranged = False
    for a, b in itertools.combinations(words,2):
        if collections.Counter(a) == collections.Counter(b):
            rearranged = True
    if rearranged == False:
        nb_passphrases_2 += 1

print(nb_passphrases, nb_passphrases_2)


