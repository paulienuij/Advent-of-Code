def validpassport(pasp):
    byr = int(pasp.split("byr:")[1].split(" ")[0])  # getting the characters between "byr:" and the next space
    iyr = int(pasp.split("iyr:")[1].split(" ")[0])
    eyr = int(pasp.split("eyr:")[1].split(" ")[0])

    # making a huge mess :(
    if 1920 <= byr <= 2002 and 2010 <= iyr <= 2020 and 2020 <= eyr <= 2030:
        # all the years are correct
        hgt = pasp.split("hgt:")[1].split(" ")[0]
        hcl = pasp.split("hcl:")[1].split(" ")[0]
        ecl = pasp.split("ecl:")[1].split(" ")[0]
        pid = pasp.split("pid:")[1].split(" ")[0]

        if hgt[-2:] not in ["cm", "in"]:
            return False
        elif hgt[-2:] == "cm" and (int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193):
            return False
        elif hgt[-2:] == "in" and (int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76):
            return False
        elif len(hcl) != 7 or hcl[0] != "#" or int(hcl[1:], 16) > int("ffffff", 16):
            return False
        elif ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        elif len(pid) != 9 or not all([c in "0123456789" for c in pid]):
            return False
        else:  # nothing seems to be wrong
            return True

    return False

with open("day04.txt") as file:
    passports = file.read().split("\n\n")

elements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid1 = 0
valid2 = 0

for pasp in passports:
    pasp = pasp.replace("\n", " ")  # remove all newlines and replace with spaces
    indices = [p.split(":")[0] for p in pasp.split(" ")]

    # create a string to test, with only the indices
    teststring = ""
    for i in indices:
        teststring = teststring + i

    if len(teststring) == 8*3:
        # all indices are there assuming no doubles
        valid1 +=1
        if validpassport(pasp):
            valid2 += 1
    elif len(teststring) == 7*3 and "cid" not in teststring:
        # there is only one missing and it is cid
        valid1 += 1
        if validpassport(pasp):
            valid2 += 1

print(valid1, valid2)
