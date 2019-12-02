with open("input.txt") as file:
    masses = file.read().splitlines()


# PART 1
def fuel_mass_1(mass):
    return max(0, (mass//3)-2)


totalfuel = sum([fuel_mass_1(int(m)) for m in masses])

print(totalfuel)


# PART2
def fuel_mass_2(m):
    mf = fuel_mass_1(m)
    if mf < 1:
        return 0
    return mf + fuel_mass_2(mf)


print(sum([fuel_mass_2(int(m)) for m in masses]))




