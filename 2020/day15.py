from collections import defaultdict

def playgame(input, end):
    pos_spoken = defaultdict(list)

    for i in (range(len(input)-1)):
        pos_spoken[input[i]].append(i)
    n = input[-1]

    for i in range(len(input)-1, end-1):
        if pos_spoken[n] == []:
            pos_spoken[n].append(i)
            n = 0
        else:
            prev = pos_spoken[n][-1]
            pos_spoken[n].append(i)
            n = i-prev
    return n

input = 6,4,12,1,20,0,16
print(playgame([6,4,12,1,20,0,16], 2020))
print(playgame([6,4,12,1,20,0,16], 30000000))

