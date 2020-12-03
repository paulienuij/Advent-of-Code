with open("day02.txt") as file:
    pwds = file.read().splitlines()

validpwds1 = 0
validpwds2 = 0

for pwd in pwds:
    check, pwd = pwd.split(": ")
    nb, letter = check.split()
    mini, maxi = [int(x) for x in nb.split("-")]

    # part 1
    amount = pwd.count(letter)
    if mini <= amount <= maxi:
        validpwds1 += 1

    # part 2
    letterstocheck = pwd[mini-1] + pwd[maxi-1]
    amount = letterstocheck.count(letter)
    if amount == 1:
        validpwds2 += 1



print(validpwds1, validpwds2)